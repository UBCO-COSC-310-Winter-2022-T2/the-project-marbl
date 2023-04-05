
SM = None
class CommandInterface:
    """
    Interact with the system through here by calling the methods,
    this will interact with the internal system methods and classes
    """
    
    def getUsernameOfCurrentlyLoggedInUser(self) -> str:
        pass
    
    def getCurrentlyLoggedInUser(self) -> str:
        pass
    
    def getCurrentChatViewed(self) -> str:
        pass
    
    def setCurrentChatViewed(self, chat: str) -> None:
        pass
    
    def Login(self, username: str, password: str) -> str:
        pass
        
    def createAccount(self, username: str, password: str, email: str) -> bool:
        pass
