
from typing import Self
from front_end.Chat import Chat


class User:

    def __init__(self, username: str, password: str, email: str):
        self._username = username
        self._password = password
        self._email = email
        self._friends : UserList = []
        self._chats : Chat = []
        self._onlineStatus = False

    def verify_password(self, entered_password: str) -> bool:
         return  self._password == entered_password

    def set_username(self, new_username: str) -> None:
        self._username = new_username

    def set_email(self,new_adress : str):
        self._email = new_adress

    def set_password(self, new_password: str) -> None:
        self._password = new_password

    def set_online_status(self, status: bool) -> None:
        self._onlineStatus = status
        
    #-----------getters----------------------
    
    def get_email(self)-> str:
        return self._email
    
    #possibly not a good idea 
    def get_password(self)-> str:
        return self._password
    
    def get_username(self) -> str:
        return self._username
    
    def get_online_status(self) -> bool:
        return self._onlineStatus
 
    def get_friends(self) -> list:
        return self._friends

    def add_friend(self, user : Self) -> bool:
        for frnd in self._friends:
            usr : User = frnd
            if(usr.get_username() == self._username):
                return False
            if(usr.get_username() == user.get_username()):
                return False
        self._friends.append(user)
        return True
            
        
    def remove_friend(self, user :  Self) -> bool:
         for frnd in self._friends:
            usr : User = frnd
            if(usr.get_username() == user.get_username()):
                self._friends.remove(user)
                return True
         
         return False

    def update_chat(self) -> None:
        pass

    def join_chat(self, chat) -> None:
        pass

    def leave_chat(self, chat) -> None:
        pass

    def send(self, chat, message) -> None:
        pass

    def receive(self, chat, message) -> None:
        pass


class UserList(list):
    
    def __init__(self, iterable=None):
        """Override initializer which can accept iterable"""
        super(UserList, self).__init__()
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, item):
        if isinstance(item, User):
            super(UserList, self).append(item)
        else:
            raise ValueError('Type User only')

    def insert(self, index, item):
        if isinstance(item, User):
            super(UserList, self).insert(index, item)
        else:
            raise ValueError('Type User only')

    def __add__(self, item):
        if isinstance(item, User):
            super(UserList, self).__add__(item)
        else:
            raise ValueError('Type User only')

    def __iadd__(self, item):
        if isinstance(item, User):
            super(UserList, self).__iadd__(item)
        else:
            raise ValueError('Type User only')