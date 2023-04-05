from SessionManager import SessionManager

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
        response = SessionManager.sign_in_with_email_and_password(username, password)
        if("error" in response):
            return (response['error']['message'])
        else:
            return (response['localId'])
        
    def createAccount(self, username: str, password: str, email: str) -> bool:
        pass
