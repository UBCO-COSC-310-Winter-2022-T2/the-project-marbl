

class Chat:

    def __init__(self, chat_id, chat_name=""):
        from front_end.User import UserList
        if chat_name == "default_chat_room":
            self.chat_name = ""
        self.chat_id = chat_id
        self.users = UserList()
        self.message_history = []
        
    # get users by doing myChat.users
    # get chat_id by doing myChat.chat_id
    
    def get_chat_name(self) -> str:
        return self.chat_name
    

    def get_message_history(self) -> list:
        return self.message_history

    def add_message_to_history(self, message) -> None:
        self.message_history.append(message)
    
    def set_message_history(self, message_history) -> None:
        self.message_history = message_history

    def add_user_to_chat(self, user) -> None:
        from front_end.User import User
        self.users.append(user)
        self.chat_name = self.chat_name + user.get_username() + " "
        

    def remove_user_from_chat(self, user) -> None:
        self.users.remove(user)


class ChatList(list):
    '''
    list of type Chat only
    '''

    def __init__(self, iterable=None):
        """Override initializer which can accept iterable"""
        super(ChatList, self).__init__()
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, item):
        if isinstance(item, Chat):
            super(ChatList, self).append(item)
        else:
            raise ValueError('Type Chat only')

    def insert(self, index, item):
        if isinstance(item, Chat):
            super(ChatList, self).insert(index, item)
        else:
            raise ValueError('Type Chat only')

    def __add__(self, item):
        if isinstance(item, Chat):
            super(ChatList, self).__add__(item)   # type: ignore
        else:
            raise ValueError('Type Chat only')

    def __iadd__(self, item):
        if isinstance(item, Chat):
            super(ChatList, self).__iadd__(item)  # type: ignore 
        else:
            raise ValueError('Type Chat only')

    def find_chat_by_id(self, id: str) -> Chat:
        for chat in self:
            if chat.chat_id == id:
                return chat
        return None  # type: ignore
