






class User:
    '''
    User Object Container. holds and is acted upon but 
    should not be a actor.
    '''
    def __init__(self, username: str, password: str, email: str):
        self._username = username
        self._password = password
        self._email = email
        self._friends = UserList()
        from front_end.Chat import ChatList
        self._chats = ChatList()
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
    
    def get_chats(self):
        return self._chats
    
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

    def add_friend(self, user) -> bool:
        '''
        #### returns
        
        false if refrence is itself or already conatians the User passed in
        '''        
        if(isinstance(user, User) == False):
            raise TypeError("only take in User type")
        peep : User = user

        for frnd in self._friends:
            usr : User = frnd
            if(usr.get_username() == self._username):
                return False
            if(usr.get_username() == peep.get_username()):
                return False
        self._friends.append(peep)
        return True
        
    def remove_friend(self, user) -> bool:
        '''
        #### returns     
        false if user does not exist
        '''
        if(isinstance(user, User) == False):
            raise TypeError("only take in User type")
        peep : User = user

        for frnd in self._friends:
            usr : User = frnd
            if(usr.get_username() == peep.get_username()):
                self._friends.remove(peep)
                return True
        return False


    def join_chat(self, chat) -> bool:
        '''
        adds user to chat if not already in it
        does so reflexsevely
        '''  
        for usr in chat.users :
             user : User = usr
             if self._username == user.get_username():
                return False
            
        #relfexitive relationship
        self._chats.append(chat)
        chat.users.append(self)
        return True
          
        

    def leave_chat(self, chat) -> bool:
        '''
        leave chat room reflexsively
        '''
        for usr in chat.users :
             user : User = usr
             if self._username == user.get_username():
                #relfexitive relationship
                self._chats.remove(chat)
                chat.users.remove(self)
                return True        

        return False    



class UserList(list):
    '''
    list that only allows users
    '''
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
            super(UserList, self).__add__(item) # type: ignore
        else:
            raise ValueError('Type User only')

    def __iadd__(self, item):
        if isinstance(item, User):
            super(UserList, self).__iadd__(item)# type: ignore
        else:
            raise ValueError('Type User only')