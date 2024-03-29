
from front_end.User import User, UserList
import importlib

 
def test_getters_setters():
   # importlib.reload(User)
    user = User('b','1','@')
    #username
    user.set_username('mlgguy1337')
    assert user.get_username() == 'mlgguy1337'

    #password
    user.set_password('password123')
    assert user.get_password() == 'password123'

    #email
    user.set_email('test@test.com')
    assert user.get_email() == 'test@test.com'

    #online status
    user.set_online_status(True)
    assert user.get_online_status() == True

def test_add_remove_friends():
    # Test adding and removing friends
    user1 = User('gamer', 'password123', 'test@test.com')
    user2 = User('janet', 'password456', 'gamee@gamee.com')

    assert user1.add_friend(user2)
    assert user1.get_friends() == [user2]

    assert user1.remove_friend(user2)
    assert len(user1.get_friends()) ==0

def test_chat_methods():
    from front_end.Chat import Chat
    # Test the methods of a User instance
    user1 = User('adam', 'adampw', 'adam@example.com')
    user2 = User('peep', 'peeppw', 'peep@example.com')

    chat1 = Chat(4)
    chat2 = Chat(5,'chat2')
    # Test joining and leaving chats
    user1.join_chat(chat1)
    user1.join_chat(chat2)
    assert user1._chats == [chat1, chat2]
    user1.leave_chat(chat1)
    assert user1._chats == [chat2]


# def test_find_by_username():
#     # Test finding a user by username
#     user1 = User('adam', 'adampw', 'adam@example.com')
#     assert User.find_user_by_username('adam') == user1
