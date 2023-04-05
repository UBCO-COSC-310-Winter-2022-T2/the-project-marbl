
class CommandInterface:
    """
    Interact with the system through here by calling the methods,
    this will interact with the internal system methods and classes
    """
    def __init__(self):
        from front_end.Getters import getSessionManager
        self.SM = getSessionManager()
        pass
    
    def getUsernameOfCurrentlyLoggedInUser(self) -> str:
        pass
    
    def getCurrentlyLoggedInUser(self) -> str:
        pass
    
    def getCurrentChatViewed(self) -> str:
        pass
    
    def setCurrentChatViewed(self, chat: str) -> None:
        pass
    
    def Login(self, username: str, password: str) -> str:
        response = self.SM.sign_in_with_email_and_password(username, password)
        if(type(response) == dict):
            #error
            ret = {"success": False, "errorMsg": response["error"]["message"]}
            return ret
        else:
            #success
            ret = {"success": True, "session": response}
            return ret
        
    def createAccount(self, username: str, password: str, email: str) -> bool:
        pass
