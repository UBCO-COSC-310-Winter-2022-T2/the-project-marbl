class Chat:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users = []
        self.message_history = []

    def get_message_history(self) -> list:
        pass

    def add_message_to_history(self, message) -> None:
        pass

    def add_user_to_chat(self, user) -> None:
        pass

    def remove_user_from_chat(self, user) -> None:
        pass

    def notify_all_users_of_chat_update(self) -> None:
        pass
