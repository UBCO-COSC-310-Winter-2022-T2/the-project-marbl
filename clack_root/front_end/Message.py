import time
from front_end.User import User

class Message:
    '''
    Holds instance data for client as a object for ui to display
    '''
    _author : User
    _date : time  # type: ignore
    _message :str
    
    def __init__(self, message: str, author : User, date:time=time.time()): # type: ignore
        '''
        create new message object with date initailizeing upon creating the object
        '''
        self._message = message
        self._date = date
        self._author = author
    
    

    def getMessage(self) -> str:
        return self._message

    def getDate(self) -> time: # type: ignore
        return self._date

    def getAuthor(self) -> User:
        return self._author

    def setMessage(self, message: str) -> None:
        self._message = message
