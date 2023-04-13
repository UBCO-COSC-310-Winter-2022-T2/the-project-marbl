import pyrebase
import json
from Getters import getMQTTClient
import User
import time

_BROKER = "test.mosquitto.org"


class Session:
    def __init__(self, idToken: str, expiry: str, refreshToken: str, isValid: bool, email: str, current_user: User):
        self.idToken = idToken
        self.expiry = expiry
        self.refreshToken = refreshToken
        self.isValid = isValid
        self.email = email
        self._current_user = current_user
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

    def getCurrentUser(self):
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

    def getUsernameOfCurrentlyLoggedInUser():
        pass

    def getCurrentlyLoggedInUser():
        pass

    def Logout():
        pass

    def ResetPassword(newPassword: str):
        pass

    def SendMessage(self, msg: str, chatid: str):
        my_mqtt_client = getMQTTClient(
            _BROKER, self.getCurrentUser.get_username())
        my_msg = {"command": "SENDMSG",
                    "author": self.getCurrentUser.get_username(),
                    "time": time.time(),
                    "message": msg}

        data_out = json.dumps(my_msg)  # encode object to JSON
        my_mqtt_client.publish("marbl/chats/"+chatid, data_out)

    def addUserToChat(username: str):
        pass

    def kickUserFromChat(username: str):
        pass

    def transferAdminship(username: str, chat: str):
        pass

    def createChat(users: str):
        pass

    def addFriend(username: str):
        pass

    def removeFriend(username: str):
        pass
