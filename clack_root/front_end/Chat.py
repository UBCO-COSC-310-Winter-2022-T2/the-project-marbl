




class Chat:
    def __init__(self, chat_id, chat_name = "chatroom"):
        from front_end.User import UserList
        self.chat_name = chat_name
        self.chat_id = chat_id
        self.users = UserList()
        self.message_history = []

    def get_message_history(self) -> list:
        return None # type: ignore

    def add_message_to_history(self, message) -> None:
        pass

    def add_user_to_chat(self, user) -> None:
        pass

    def remove_user_from_chat(self, user) -> None:
        pass

    def notify_all_users_of_chat_update(self) -> None:
        pass


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
            super(ChatList, self).__add__(item) # type: ignore
        else:
            raise ValueError('Type Chat only')

    def __iadd__(self, item):
        if isinstance(item, Chat):
            super(ChatList, self).__iadd__(item) # type: ignore
        else:
            raise ValueError('Type Chat only')