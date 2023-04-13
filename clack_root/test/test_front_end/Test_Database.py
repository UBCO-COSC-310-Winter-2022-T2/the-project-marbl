import pyrebase
from front_end.Getters import get_database
from unittest.mock import patch, Mock
from front_end.Getters import get_firebase_connection

def test_init():
    pyrebase.initialize_app = Mock()
    db = get_database().db
    assert db is not None

def test_get_user_info():
    pyrebase.initialize_app = Mock()
    db = get_database()

    assert db.get_info_from_username('test_user') is not None
    assert not db.get_info_from_username([])

def test_add_to_friends_list():
    pyrebase.initialize_app = Mock()
    db = get_database()
    assert db.add_to_friends_list('test_user', 'horse_friend') is not None
    assert not db.add_to_friends_list('', '')

def test_remove_from_friends_list():
    pyrebase.initialize_app = Mock()
    db = get_database()
    assert db.remove_from_friends_list('test_user', 'horse_friend') is not None
    assert not db.remove_from_friends_list('', '')

def test_get_friends_from_username():
    pyrebase.initialize_app = Mock()
    db = get_database()
    assert db.get_friends_from_username('test_user') is not None
    assert not db.get_friends_from_username('')
