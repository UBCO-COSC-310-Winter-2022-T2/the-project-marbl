import json
from front_end.User import User
from front_end.SessionManager import SessionManager
import pytest
import pyrebase
from unittest.mock import patch, Mock
from front_end.Session import Session
from front_end.Getters import getMQTTClient
from front_end.Getters import getSessionManager
import time


def test_send_receive_message():
    # NOTE: once sign_in_with_email_and_password is implemented properly with User being given a proper username, this will need to be changed so the username corresponding with paswordis123456@test.com is the same

    # first login for a user
    mySM = getSessionManager()
    response1 = mySM.sign_in_with_email_and_password(
        'passwordis123456@test.com', '123456')
    # check to make sure we got a Session and not an error
    assert type(response1) == Session
    mySession = mySM.get_existing_session()
    assert mySession is not None

    # subscribe user to chat
    mySession.subscribe_to_topic('marbl/chats/test_chat_room')

    # send the chat
    mySession.SendMessage("erg", 'test_chat_room')

    # wait a couple secs
    time.sleep(2)

    # now check to see that the user recieved it
    myUser = mySession.getCurrentUser()
    myChat = myUser.get_chats().find_chat_by_id('test_chat_room')
    string_of_all_msgs = ''
    for msg in myChat.get_message_history():
        string_of_all_msgs = string_of_all_msgs + msg.getMessage()
    assert "erg" in string_of_all_msgs