from front_end.Chat import Chat
from front_end.User import User, UserList


def test_message_history():
    mychat = Chat("123")
    mychat.add_message_to_history("my cool message")
    mymessagehistory = mychat.get_message_history()
    assert mymessagehistory == ["my cool message"]

    mychat.add_message_to_history("my cool message2")
    mymessagehistory = mychat.get_message_history()
    assert mymessagehistory == ["my cool message", "my cool message2"]


def test_add_user_to_chat():
    #create chat
    mychat = Chat("123", "default_chat_room")
    
    #add first user to chat
    testUser = User("user1", "password", "email@email.com")
    mychat.add_user_to_chat(testUser)
    myuserlist = mychat.users
    
    # check to make sure the user was added
    assert len(myuserlist) == 1
    myusersstring = ""
    for user in myuserlist:
        myusersstring = myusersstring + user.get_username()
    assert myusersstring == "user1"
    
    # add second user
    testUser = User("user2", "password", "email@email.com")
    mychat.add_user_to_chat(testUser)
    myuserlist = mychat.users
    
    # check to make sure the user was added
    assert len(myuserlist) == 2
    myusersstring = ""
    for user in myuserlist:
        myusersstring = myusersstring + user.get_username()
    assert myusersstring == "user1user2"

    # TODO: add another test case to make sure you cannot add the same user twice
    