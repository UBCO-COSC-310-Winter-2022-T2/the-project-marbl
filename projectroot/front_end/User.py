class User:
    def __init__(self, username: str, password: str, email: str):
        self._username = username
        self._password = password
        self._email = email
        self._friends = []
        self._chats = []
        self._onlineStatus = False

    def get_username(self) -> str:
        pass

    def set_username(self, new_username: str) -> None:
        pass

    def verify_password(self, entered_password: str) -> bool:
        pass

    def set_password(self, new_password: str) -> None:
        pass

    def set_online_status(self, status: bool) -> None:
        pass

    def get_online_status(self) -> bool:
        pass

    def notify_friends_of_your_status(self) -> None:
        pass

    def get_friends(self) -> list:
        pass

    def add_friend(self, username: str) -> bool:
        pass

    def remove_friend(self, friend) -> bool:
        pass

    def update_chat(self) -> None:
        pass

    def join_chat(self, chat) -> None:
        pass

    def leave_chat(self, chat) -> None:
        pass

    def find_user_by_username(self, username: str) -> str:
        pass

    def send(self, chat, message) -> None:
        pass

    def receive(self, chat, message) -> None:
        pass

