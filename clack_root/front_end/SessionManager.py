import json
from front_end.Session import Session
from front_end.FirebaseConnection import FirebaseConnection

class SessionManager:
  def __init__(self):
    self.firebase = FirebaseConnection()
    self.auth = self.firebase.get_auth_connection()
    self.database = self.firebase.get_database_connection()
    self.existingSession = None

  def get_existing_session(self):
    return self.existingSession
  
  def sign_in_with_email_and_password(self, email, password): #session expires every hour, refresh with user = auth.refresh(user['refreshToken'])
    try:
      response = self.auth.sign_in_with_email_and_password(email, password)
      self.existingSession = Session(response['idToken'], response['expiresIn'], response['refreshToken'], response['registered'], response['email'])
      return self.existingSession
    except Exception as e:
      return json.loads(e.strerror)
  
  def forgot_password(self, email):
    try:
      response = self.auth.send_password_reset_email(email)
      response["success"] = True
      return response
    except Exception as e:
      return json.loads(e.strerror)
    
  def create_account(self, email, password, username, first_name, last_name):
    user = {}

    #try to save data about user (checks if username already exists)
    try:
      self.save_user_data(username, first_name, last_name, email)
    except Exception as e:
      print("DATABASE ERROR:", e)
      return {"error": {"message": str(e)}}
    
    #try to create account
    try:
      user = self.auth.create_user_with_email_and_password(email, password)
      return user
    except Exception as e:
      self.database.remove_account_data(username)
      return json.loads(e.strerror)
  
  def save_user_data(self, username, first_name, last_name, email):
    if(len(username) < 3):
        raise Exception("Username must be at least 3 characters long. This really should not happen!")
    if(len(first_name) < 1):
        raise Exception("First name must be at least 1 character long. This really should not happen!")
    if(len(last_name) < 1):
        raise Exception("Last name must be at least 1 character long. This really should not happen!")
    
    data = {
    "status" : True,
    "first_name": first_name,
    "last_name": last_name,
    "email": email
    }
    # Set the UID key in the database to the user data
    if(self.database.get_username_exists(username)):
      raise Exception("Username exists already :(")
    else:
      if(self.database.create_user_with_data(username,data)):
        return True
      else:
        raise Exception("Error creating user ??? why")