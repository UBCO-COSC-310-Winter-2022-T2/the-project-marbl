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
class SessionManager:
  def __init__(self):
    self.auth = auth
    self.existingSession = None
  def get_existing_session(self):
    return self.existingSession
  def sign_in_with_email_and_password(self, email, password):
    try:
      response = self.auth.sign_in_with_email_and_password(email, password)
      self.existingSession = Session(response['idToken'], response['expiresIn'], response['refreshToken'], response['registered'], response['email'])
      return self.existingSession
    except Exception as e:
      return json.loads(e.strerror)
    #session expires every hour, refresh with user = auth.refresh(user['refreshToken'])

  def create_user_with_email_and_password(self, email, password):
    try:
      user = self.auth.create_user_with_email_and_password(email, password)
      return user
    except Exception as e:
      return json.loads(e.strerror)