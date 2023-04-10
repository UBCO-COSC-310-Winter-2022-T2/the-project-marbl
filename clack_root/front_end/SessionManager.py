import pyrebase
import json
from front_end.Session import Session

config = {
  "apiKey": "AIzaSyAT_ILhmjVI1gv9qdWrfsFaxJSt8cvNsSw",
  "authDomain": "cosc310-marbl.firebaseapp.com",
  "databaseURL": "https://cosc310-marbl-default-rtdb.firebaseio.com",
  "storageBucket": "cosc310-marbl.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

class SessionManager:
  def __init__(self):
    self.auth = auth
    self.database = database
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
    
  def create_account(self, email, password, username, first_name, last_name):
    user = {}

    #try to save data about user (checks if username already exists)
    try:
      self.save_user_data(username, first_name, last_name)
    except Exception as e:
      print("DATABASE ERROR:", e)
      self.clear_user_data(username)
      return {"error": {"message": str(e)}}
    
    #try to create account
    try:
      user = self.auth.create_user_with_email_and_password(email, password)
      return user
    except Exception as e:
      self.clear_user_data(username)
      return json.loads(e.strerror)
  
  def save_user_data(self, username, first_name, last_name):
    if(len(username) < 3):
        raise Exception("Username must be at least 3 characters long. This really should not happen!")
    if(len(first_name) < 1):
        raise Exception("First name must be at least 1 character long. This really should not happen!")
    if(len(last_name) < 1):
        raise Exception("Last name must be at least 1 character long. This really should not happen!")
    
    data = {
    "first_name": first_name,
    "last_name": last_name,
    "username": username
    }
    # Set the UID key in the database to the user data
    if(self.get_username_exists(username)):
      raise Exception("Username exists already :(")
    else:
      return database.child("users").child(username).set(data)
  
  def clear_user_data(self,username):
    if(self.get_username_exists(username)):
      database.child("users").child(username).set(None)
  
  def get_username_exists(self, username):
    if(database.child('users').child(username).get().val()):
      return True
    else:
      return False