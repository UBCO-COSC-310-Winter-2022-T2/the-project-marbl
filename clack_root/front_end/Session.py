import pyrebase
import json
from front_end.User import User
import time



from front_end.User import User
import time



class Session:
    def __init__(self, idToken: str, expiry: str, refreshToken: str, isValid: bool, email: str, current_user: User):
        self.idToken = idToken
        self.expiry = expiry
        self.refreshToken = refreshToken
        self.isValid = isValid
        self.email = email
        self._current_user = current_user
        from front_end.Getters import getMQTTClient
<<<<<<< HEAD
        self._mqtt_client = getMQTTClient("test.mosquitto.org", current_user.get_username()) # type: ignore
=======
        self._mqtt_client = getMQTTClient("test.mosquitto.org", current_user.get_username())
>>>>>>> 9bfee9b4e3d731ea6392b2b5e074ebbc7369c336
        
    # getters

    def getIdToken(self):
        return self.idToken

    def getExpiry(self):
        return self.expiry

    def getRefreshToken(self):
        return self.refreshToken

    def getIsValid(self):
        return self.isValid

    def getEmail(self):
        return self.email

    def getCurrentUser(self) -> User:
        return self._current_user
      
    # setters

    def setIdToken(self, idToken: str):
        self.idToken = idToken

    def setExpiry(self, expiry: str):
        self.expiry = expiry

    def setRefreshToken(self, refreshToken: str):
        self.refreshToken = refreshToken

    def setIsValid(self, isValid: bool):
        self.isValid = isValid

    def setEmail(self, email: str):
        self.email = email
    # methods

    def getUsernameOfCurrentlyLoggedInUser(): # type: ignore
        pass

    def Logout(): # type: ignore
        pass

    def ResetPassword(newPassword: str): # type: ignore
        pass

    def SendMessage(self, msg: str, chatid: str):
        my_msg = {"command": "SENDMSG",
                    "author": self._current_user.get_username(),
                    "time": time.time(),
                    "message": msg}
        data_out = json.dumps(my_msg)  # encode object to JSON
        self._mqtt_client.publish("marbl/chats/"+chatid, data_out, 2)

    def subscribe_to_topic(self, topic: str):
        self._mqtt_client.subscribe(topic)
    
<<<<<<< HEAD
    def addUserToChat(username: str): # type: ignore
        pass

    def kickUserFromChat(username: str): # type: ignore
        pass

    def transferAdminship(username: str, chat: str): # type: ignore
        pass

    def createChat(users: str): # type: ignore
        pass

    def addFriend(username: str): # type: ignore
        pass

    def removeFriend(username: str):# type: ignore
        pass

    def update_subscriptions(self):
        for chat in self._current_user.get_chats():
            self.subscribe_to_topic("marbl/chats/"+chat.chat_id)
    

