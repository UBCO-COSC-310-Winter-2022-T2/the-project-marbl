class Database:
  def __init__(self):
    from front_end.Getters import get_firebase_connection
    self.firebasecon = get_firebase_connection()
    self.db = self.firebasecon.get_database_connection()
    