
class CommandInterface:
    """
    Interact with the system through here by calling the methods,
    this will interact with the internal system methods and classes
    """
    def __init__(self):
        from front_end.Getters import getSessionManager
        self.SM = getSessionManager()
    
    def getUsernameOfCurrentlyLoggedInUser(self) -> str:
        return ""
    
    def getCurrentlyLoggedInUser(self) -> str:
        return ""
    
    def getCurrentChatViewed(self) -> str:
        return ""
    
    def setCurrentChatViewed(self, chat: str) -> None:
        pass
    
    def login(self, email: str, password: str) -> str:
        response = self.SM.sign_in_with_email_and_password(email, password)
        if(type(response) == dict):
            #error
            ret = {"success": False, "error": response["error"]}
            return ret # type: ignore
        else:
            #success
            ret = {"success": True, "session": response}
            return ret # type: ignore
        
    def create_account(self, email: str, password: str, username: str, first_name: str, last_name: str) -> bool:

        if(len(username) < 3):
            return {"success": False, "error": {"message": "Username must be at least 3 characters long"}} # type: ignore
        if(len(first_name) < 1):
            return {"success": False, "error": {"message": "First name must be at least 1 character long"}} # type: ignore
        if(len(last_name) < 1):
            return {"success": False, "error": {"message": "Last name must be at least 1 character long"}} # type: ignore
        
        
        response = self.SM.create_account(email, password, username, first_name, last_name)

        if("error" in response):
            #error
            ret = {"success": False, "error": response["error"]}
            return ret # type: ignore
        else:
            #success
            ret = {"success": True}
            return ret # type: ignore
    def forgot_password(self,email:str):
        response = self.SM.forgot_password(email)
        if("error" in response):
            #error
            ret = {"success": False, "error": response["error"]}
            return ret
        else:
            #success
            ret = {"success": True}
            return ret