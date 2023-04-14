import json
import datetime
from front_end.Message import Message
from front_end.User import User,UserList
import traceback
import sys
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
    
    ######### User functions ###########
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
    
    def get_username_from_email(self, email: str):
        try:
            #loop through all users
            for user in self.db.child("users").get().each():
                if("email" in self.convert_ordered_dict_to_dict(user.val())):
                    this_email = self.convert_ordered_dict_to_dict(user.val())["email"]
                    username = user.key()
                    if(this_email == email):
                        return username
            return None
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
        
    # deletes user information in the realtime database, but their account
    # is not deleted in firebase
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
            print("create_user_with_data error:", e)
            return False
    
    def set_status_by_username(self,username : str, state : bool):
        try:
            self.db.child("users").child(username).child("status").set(state)
            return True
        except Exception as e:
            print("DATABASE ERROR:", e)
            return False
    
    def get_status_by_username(self,username : str):
        try:
            status = self.db.child("users").child(username).child("status").get()
            status = self.convert_ordered_dict_to_dict(status.val())
            return status
        except Exception as e:
            print("DATABASE ERROR:", e)
            return None
    
    ######### Chat functions ###########

    def send_message_to_chat(self,chat_id,username,message):
        try:
            message_data = {
                "author": username,
                "message": message,
                "time": str(datetime.datetime.now())
            }
            self.db.child("chats").child(chat_id).child("messages").push(message_data)
            return True
        except Exception as e:
            print("DATABASE ERROR:", e)
            return False
    def get_message_objects_from_chat(self,chat_id):
        try:
            messages = self.db.child("chats").child(chat_id).child("messages").get()
            messages = self.convert_ordered_dict_to_dict(messages.val())
            message_array = []
            for msg in messages.values():
                message_array.append(Message(msg["author"],msg["message"]))
            return message_array
        except Exception as e:
            print("DATABASE ERROR:", e)
            return []
    def get_user_list_from_chat(self,chat_id):
        try:
            users = self.db.child("chats").child(chat_id).child("users").get()
            users = self.convert_ordered_dict_to_dict(users.val())
            user_list = UserList()
            for user in users.keys():
                user_list.append(User(user,"external_user","external_user"))
            return user_list
        except Exception as e:
            print(traceback.format_exc())
            print("DATABASE ERROR:", e)
            return UserList()
    def get_chats_by_username(self,username):
        try:
            chats = self.db.child("users").child(username).child("chats").get()
            if(chats.val()):
                chats = list(self.convert_ordered_dict_to_dict(chats.val()).keys())
                return chats
            return []
        except Exception as e:
            print(traceback.format_exc())
            print("DATABASE ERROR:", e)
            return []
    def get_chat_info_by_chat_id(self,chat_id):
        try:
            chat_info = self.db.child("chats").child(chat_id).get()
            chat_info = self.convert_ordered_dict_to_dict(chat_info.val())
            return chat_info
        except Exception as e:
            print("DATABASE ERROR:", e)
            return None
    
    def add_user_to_group_chat(self,username,chat_id):
        try:
            self.db.child("users").child(username).child("chats").child(chat_id).set({"cool": True})
            self.db.child("chats").child(chat_id).child("users").child(username).set({"cool": True})
            return True
        except Exception as e:
            print("DATABASE ERROR:", e)
            return False
    def create_group_chat(self,chat_name):
        try:
            self.db.child("chats").push({"chat_name": chat_name})
            return True
        except Exception as e:
            print("DATABASE ERROR:", e)
            return False
    def get_all_group_chats(self):
        try:
            chats = self.db.child("chats").get()
            chats = self.convert_ordered_dict_to_dict(chats.val())
            return list(chats.keys())
        except Exception as e:
            print(traceback.format_exc())
            print("DATABASE ERROR:", e)
            return None
    
    