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
    
  def save_user_data(self, username, first_name, last_name, UID):
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
    return database.child("users").child(UID).set(data)
    
  def create_account(self, email, password, username, first_name, last_name):
    user = {}
    try:
      user = self.auth.create_user_with_email_and_password(email, password)
    except Exception as e:
      return json.loads(e.strerror)
    
    try:
      self.save_user_data(username, first_name, last_name, user['localId'])
      return user
    except Exception as e:
      print("DATABASE ERROR:", e)
      return {"error": {"message": "Error saving user data"}}