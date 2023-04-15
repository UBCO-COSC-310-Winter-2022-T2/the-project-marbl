
from front_end.Chat import Chat

class GroupChat(Chat):
    def __init__(self, chatId, admin, chatName):
        super().__init__(chatId)
        self.admin = admin
        self.chatName = chatName

    def set_chat_name(self, name):
        pass

    def get_chat_name(self):
        pass

    def get_admin(self):
        pass

    def set_admin(self, user):
        pass
