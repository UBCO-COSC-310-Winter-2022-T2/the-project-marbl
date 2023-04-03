import pyrebase
import json

config = {
  "apiKey": "AIzaSyAT_ILhmjVI1gv9qdWrfsFaxJSt8cvNsSw ",
  "authDomain": "cosc310-marbl.firebaseapp.com",
  "databaseURL": "https://cosc310-marbl-default-rtdb.firebaseio.com",
  "storageBucket": "cosc310-marbl.appspot.com"
}

class FirebaseAuthentication:
  def __init__(self):
    self.firebase = pyrebase.initialize_app(config)
    self.auth = self.firebase.auth()

  def sign_in_with_email_and_password(self, email, password):
    try:
      user = self.auth.sign_in_with_email_and_password(email, password)
      return user
    except Exception as e:
      return json.loads(e.strerror)
    #session expires every hour, refresh with user = auth.refresh(user['refreshToken'])

  def create_user_with_email_and_password(self, email, password):
    try:
      user = self.auth.create_user_with_email_and_password(email, password)
      return user
    except Exception as e:
      return json.loads(e.strerror)