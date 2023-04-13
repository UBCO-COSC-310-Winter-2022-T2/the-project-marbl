import pyrebase
from front_end.Getters import get_firebase_connection
from unittest.mock import patch, Mock

def test_init():
    pyrebase.initialize_app = Mock()
    db = get_firebase_connection().get_database_connection().db
    assert db is not None

def test_get_user_info():
    pyrebase.initialize_app = Mock()
    db = get_firebase_connection().get_database_connection().db

    assert db.get_info_from_username('test_user') is not None

def test_add_to_friends_list():
    pyrebase.initialize_app = Mock()
    db = get_firebase_connection().get_database_connection().db
    assert db.add_to_friends_list('test_user', 'horse_friend') is not None

def test_remove_from_friends_list():
    pyrebase.initialize_app = Mock()
    db = get_firebase_connection().get_database_connection().db
    assert db.remove_from_friends_list('test_user', 'horse_friend') is not None

def test_get_friends_from_username():
    pyrebase.initialize_app = Mock()
    db = get_firebase_connection().get_database_connection().db
    assert db.get_friends_from_username('test_user') is not None

import collections

def test_convert_ordered_dict_to_dict():
    ordered_dict = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    from front_end.Database import Database
    Database.__init__ = Mock(return_value=None)
    db = Database("asd")
    result = db.convert_ordered_dict_to_dict(ordered_dict)
    assert result == {'a': 1, 'b': 2, 'c': 3}

def test_get_group_chats_for_username():
    pyrebase.initialize_app = Mock()
    db = get_firebase_connection().get_database_connection().db
    assert db.get_group_chats_for_username('test_user') is not None