from front_end.Getters import get_firebase_connection
from unittest.mock import patch, Mock

def test_init():
    fc = get_firebase_connection()
    fc.firebase.initialize_app = Mock()
    fc.firebase_connection is not None

def test_get_database_connection():
    fc = get_firebase_connection()
    fc.firebase.initialize_app = Mock()
    fc.firebase.database = Mock()
    assert fc.get_database_connection() is not None

def test_get_auth_connection():
    fc = get_firebase_connection()
    fc.firebase.initialize_app = Mock()
    fc.firebase.auth = Mock()
    assert fc.get_auth_connection() is not None