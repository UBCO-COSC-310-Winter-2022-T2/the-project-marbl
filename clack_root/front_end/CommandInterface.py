class CommandInterface:
    """
    Interact with the system through here by calling the methods,
    this will interact with the internal system methods and classes
    """
    
    def getUsernameOfCurrentlyLoggedInUser(self) -> str:
        pass
    
    def getCurrentlyLoggedInUser(self) -> User:
        pass
    
    def getCurrentChatViewed(self) -> Chat:
        pass
    
    def setCurrentChatViewed(self, chat: Chat) -> None:
        pass
    
    def Login(self, username: str, password: str) -> bool:
        pass
    
    def Logout(self) -> None:
        pass
    
    def ResetPassword(self, newPassword: str) -> None:
        pass
    
    def SendMessage(self, msg: str) -> None:
        pass
    
    def addUserToChat(self, username: str) -> None:
        pass
    
    def kickUserFromChat(self, username: str) -> None:
        pass
    
    def transferAdminship(self, username: str, chat: Chat) -> None:
        pass
    
    def createChat(self, users: List[User]) -> None:
        pass
    
    def createAccount(self, username: str, password: str, email: str) -> bool:
        pass
    
    def addFriend(self, username: str) -> bool:
        pass
    
    def removeFriend(self, username: str) -> None:
        pass
    
    def getFriends(self) -> List[User]:
        pass
