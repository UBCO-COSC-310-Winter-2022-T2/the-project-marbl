import json
class Database:
    def __init__(self,connection):
        self.db = connection.database()

    def convert_ordered_dict_to_dict(self, ordered_dict):
        try:
            my_dict = json.loads(json.dumps(ordered_dict))
            return my_dict
        except Exception as e:
            print("dict conversion error:", e)
            return {}
    
    def get_username_exists(self,username: str):
        if(self.get_info_from_username(username) is not None):
            return True
        else:
            return False

    def get_info_from_username(self, username: str):
        if (len(username) < 3):
            return None
        try:
            info = self.db.child("users").child(username).get()
            info = self.convert_ordered_dict_to_dict(info.val())
            return info
        except Exception as e:
            print("DATABASE ERROR:", e)
            return None

    def add_to_friends_list(self, adding_username1, added_username2):
        if (len(adding_username1) < 3 or len(added_username2) < 3):
            return False
        try:
            self.db.child("users").child(adding_username1).child("friends").child(
                added_username2).set({"cool": True})  # needs a key so cool: true as a placeholder :D
            return True
        except Exception as e:
            print("DATABASE ERROR:", e)
            return False

    def remove_from_friends_list(self, removing_username, removed_username):
        if (len(removing_username) < 3 or len(removed_username) < 3):
            return False
        try:
            self.db.child("users").child(removing_username).child(
                "friends").child(removed_username).set(None)
            return True
        except Exception as e:
            print("DATABASE ERROR:", e)
            return False
    
    def get_friends_from_username(self, username: str):
        if (len(username) < 3):
            return False
        try:
            friends = self.db.child("users").child(username).child("friends").get()
            friends = self.convert_ordered_dict_to_dict(friends.val())
            return friends
        except Exception as e:
            print("DATABASE ERROR:", e)
            return None
        
    def remove_account_data(self, username):
        try:
            self.db.child("users").child(username).set(None)
            return True
        except Exception as e:
            print("DATABASE ERROR:", e)
            return False
    
    def create_user_with_data(self,username,data):
        try:
            self.db.child("users").child(username).set(data)
            return True
        except Exception as e:
            print("DATABASE ERROR:", e)
            return False
