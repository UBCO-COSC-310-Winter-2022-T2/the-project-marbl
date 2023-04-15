import json
import requests
from front_end.Session import Session
from front_end.FirebaseConnection import FirebaseConnection
from front_end.User import User
from front_end.Chat import Chat


class SessionManager:
    def __init__(self):
        self.firebase = FirebaseConnection()
        self.auth = self.firebase.get_auth_connection()
        self.database = self.firebase.get_database_connection()
        self.existingSession = None

    def get_existing_session(self):
        return self.existingSession

    # session expires every hour, refresh with user = auth.refresh(user['refreshToken'])
    def sign_in_with_email_and_password(self, email, password):
        try:
            response = self.auth.sign_in_with_email_and_password(
                email, password)
            if ("email" in response and response["email"] == email):
                username = self.database.get_username_from_email(
                    email) or "anon"
                if(username == "anon"):
                    print("User does not exist in database, they are probably an old account. Functions may not work properly.")
                my_user = User(username, "password123", email)
                self.populate_user_with_chats(my_user)
                self.populate_user_with_friends(my_user)
                print("User object created:")
                print(vars(my_user))
                self.existingSession = Session(
                    response['idToken'], response['expiresIn'], response['refreshToken'], response['registered'], response['email'], my_user)
                
                # subscribe users to the chats they're in
                self.existingSession.update_subscriptions()
                
                return self.existingSession
        except requests.HTTPError as e:
            return json.loads(e.strerror)

    def populate_user_with_chats(self, user_object):
        # get all chats user is in
        chat_ids = self.database.get_chats_by_username(
            user_object.get_username())
        if (not chat_ids):
            return
        for chat_id in chat_ids:
            data = self.database.get_chat_info_by_chat_id(chat_id)
            if (data):
                chat_name = data["chat_name"]
                my_chat = Chat(chat_id, chat_name)  # create chat object
                all_messages = self.database.get_message_objects_from_chat(
                    chat_id)
                # set message history of chat
                my_chat.set_message_history(all_messages)
                all_users = self.database.get_user_list_from_chat(
                    chat_id)  # get user list of chat
                for user in all_users:
                    if (user.get_username() == user_object.get_username()):
                        user_object.join_chat(my_chat)
                    else:
                        # add user to chat if not already in
                        user.join_chat(my_chat)

    def populate_user_with_friends(self, user_object):
        friends = self.database.get_friends_from_username(
            user_object.get_username())
        if (not friends):
            return
        for friend in friends:
            user_object.add_friend(friend)

    def forgot_password(self, email):
        try:
            response = self.auth.send_password_reset_email(email)
            response["success"] = True
            return response
        except requests.HTTPError as e:
            return json.loads(e.strerror)

    def create_account(self, email, password, username, first_name, last_name):
        user = {}

        # try to save data about user (checks if username already exists)
        try:
            self.save_user_data(username, first_name, last_name, email)
        except Exception as e:
            print("DATABASE ERROR:", e)
            return {"error": {"message": str(e)}}

        # try to create account
        try:
            user = self.auth.create_user_with_email_and_password(
                email, password)
            return user
        except requests.HTTPError as e:
            self.database.remove_account_data(username)
            return json.loads(e.strerror)

    def save_user_data(self, username, first_name, last_name, email):
        if (len(username) < 3):
            raise Exception(
                "Username must be at least 3 characters long. This really should not happen!")
        if (len(first_name) < 1):
            raise Exception(
                "First name must be at least 1 character long. This really should not happen!")
        if (len(last_name) < 1):
            raise Exception(
                "Last name must be at least 1 character long. This really should not happen!")

        data = {
            "status": True,
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        # Set the UID key in the database to the user data
        if (self.database.get_username_exists(username)):
            raise Exception("Username exists already :(")
        else:
            if (self.database.create_user_with_data(username, data)):
                return True
            else:
                raise Exception("Error creating user ??? why")
