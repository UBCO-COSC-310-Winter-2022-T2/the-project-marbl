import pyrebase
from front_end.Database import Database

class FirebaseConnection:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyAT_ILhmjVI1gv9qdWrfsFaxJSt8cvNsSw",
            "authDomain": "cosc310-marbl.firebaseapp.com",
            "databaseURL": "https://cosc310-marbl-default-rtdb.firebaseio.com",
            "storageBucket": "cosc310-marbl.appspot.com"
        }
        self.firebase = pyrebase
        self.firebase_connection = self.firebase.initialize_app(self.config)
        self.database = None
        self.auth = None

    def get_database_connection(self):
         if(self.database):
             return self.database
         else:
             self.database = Database(self.firebase_connection)
             return self.database
    def get_auth_connection(self):
         if(self.auth):
             return self.auth
         else:
             self.auth = self.firebase_connection.auth()
             return self.auth
