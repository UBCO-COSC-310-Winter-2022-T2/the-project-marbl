import time
from datetime import datetime
from front_end.User import User

class Message:
    '''
    Holds instance data for client as a object for ui to display
    '''
    _author : User
    _time : float  
    _message :str
    
    def __init__(self, message: str, author : User, time: float = time.time()): 
        '''
        create new message object with date initailizeing upon creating the object
        '''
        
        self._message = message
        self._time = time
        self._author = author
    
    

    def getMessage(self) -> str:
        return self._message

    def getDate(self) -> float: 
        return self._time

    def getDateTime(self) -> datetime:
        return datetime.fromtimestamp(self._time)

    def getAuthor(self) -> User:
        return self._author

    def setMessage(self, message: str) -> None:
        self._message = message
