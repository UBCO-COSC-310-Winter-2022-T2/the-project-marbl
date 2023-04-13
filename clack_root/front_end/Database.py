class Database:
  def __init__(self):
    from front_end.Getters import get_firebase_connection
    self.firebasecon = get_firebase_connection()
    self.db = self.firebasecon.get_database_connection()

  def get_info_from_username(self, username : str):
    pass
    #return self.db.child("users").child(username).get()
  def add_to_friends_list(self, username,to_be_added_username):
    pass
    #self.database.child("users").child(username).child("friends").child("horse_friend").set({"cool":True})
