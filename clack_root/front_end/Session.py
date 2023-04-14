import pyrebase
import json

from clack_root.front_end import User

class Session:

  def __init__(self,idToken: str, expiry : str, refreshToken: str, isValid: bool, email: str):
    self.idToken = idToken
    self.expiry = expiry
    self.refreshToken = refreshToken
    self.isValid = isValid
    self.email = email
  ##getters
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
  ##setters
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
  ##methods
  def getUsernameOfCurrentlyLoggedInUser():
    pass
  def getCurrentlyLoggedInUser() -> User:
    return User.User("frank","123", "b@b")
  def Logout():
    pass
  def ResetPassword(newPassword: str):
    pass
  def SendMessage(msg: str):
    pass
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
