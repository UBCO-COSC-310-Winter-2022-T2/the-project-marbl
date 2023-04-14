from front_end.Chat import Chat, ChatList

def test_find_chat_by_id():
    # add a chat to the list
    test_chats = ChatList()
    chat1 = Chat("1234")
    test_chats.append(chat1)
    
    # find the chat
    mychat = test_chats.find_chat_by_id("1234")
    assert mychat == chat1