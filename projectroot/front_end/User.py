class User:
    def __init__(self, username: str, password: str, email: str):
        self._username = username
        self._password = password
        self._email = email
        self._friends = []
        self._chats = []
        self._onlineStatus = False

    def getUsername(self) -> str:
        pass

    def setUsername(self, newUsername: str) -> None:
        pass

    def verifyPassword(self, enteredPassword: str) -> bool:
        pass

    def setPassword(self, newPassword: str) -> None:
        pass

    def setOnlineStatus(self, status: bool) -> None:
        pass

    def getOnlineStatus(self) -> bool:
        pass

    def notifyFriendsOfYourStatus(self) -> None:
        pass

    def getFriends(self) -> List['User']:
        pass

    def addFriend(self, username: str) -> bool:
        pass

    def removeFriend(self, friend: 'User') -> bool:
        pass

    def updateChat(self) -> None:
        pass

    def send(self, chat: 'Chat', message: str) -> None:
        pass

    def receive(self, chat: 'Chat', message: Message) -> None:
        pass

    def joinChat(self, chat: 'Chat') -> None:
        pass

    def leaveChat(self, chat: 'Chat') -> None:
        pass

    def findUserByUsername(self, username: str) -> 'User':
        pass
