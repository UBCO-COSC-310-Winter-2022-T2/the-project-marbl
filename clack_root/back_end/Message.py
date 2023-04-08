
import datetime as date
import back_end.User as usr 

class Message:
    '''    
    Contains user text informational data
    
    '''
    _text : str
    _date : date.datetime
    _user : usr.User
    ##------Constructors-------
    def __init__(self, text : str):
        pass
    def __init__(self):
        pass
    def __init__(self, text : str, sender : usr.User, date : date.datetime=date.datetime(2000,1,1)):
        pass
    
    def toString(this):
        return None
    ##-----getters---------
    def getMessage(this) -> str:
        return None
    def getUser(this) -> usr.User:
        return None
    def getDate(this) -> date.datetime:
        return None
    ##-----setters---------
    def setMessage(this, message : str):
        pass
    