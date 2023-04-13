import pyrebase


class FirebaseConnection:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyAT_ILhmjVI1gv9qdWrfsFaxJSt8cvNsSw",
            "authDomain": "cosc310-marbl.firebaseapp.com",
            "databaseURL": "https://cosc310-marbl-default-rtdb.firebaseio.com",
            "storageBucket": "cosc310-marbl.appspot.com"
        }
        self.pyrebase_connection = pyrebase.initialize_app(self.config)

    def getDatabaseConnection(self):
         pass
