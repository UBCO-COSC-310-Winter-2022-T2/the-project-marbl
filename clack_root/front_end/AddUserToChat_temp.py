from front_end.Database import Database
from front_end.FirebaseConnection import FirebaseConnection
from front_end.Getters import get_firebase_connection


# use this to create chats and add users to chats (use until we finish the add user to chat use case)
mydbconn = get_firebase_connection()
mydb = mydbconn.get_database_connection()
mychatid = mydb.create_group_chat("default_chat_room")
mydb.add_user_to_group_chat("example_username2", mychatid['name'])

