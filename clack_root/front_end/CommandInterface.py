
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
    
    def Login(self, email: str, password: str) -> str:
        response = self.SM.sign_in_with_email_and_password(email, password)
        if(type(response) == dict):
            #error
            ret = {"success": False, "errorMsg": response["error"]["message"]}
            return ret
        else:
            #success
            ret = {"success": True, "session": response}
            return ret
        
    def createAccount(self, email: str, password: str, username: str, first_name: str, last_name: str) -> bool:

        if(len(username) < 3):
            return {"success": False, "error": {"message": "Username must be at least 3 characters long"}}
        if(len(first_name) < 1):
            return {"success": False, "error": {"message": "First name must be at least 1 character long"}}
        if(len(last_name) < 1):
            return {"success": False, "error": {"message": "Last name must be at least 1 character long"}}
        
        
        response = self.SM.create_user_with_email_and_password(email, password, username, first_name, last_name)

        if("error" in response):
            #error
            ret = {"success": False, "errorMsg": response["error"]["message"]}
            return ret
        else:
            #success
            ret = {"success": True}
            return ret
