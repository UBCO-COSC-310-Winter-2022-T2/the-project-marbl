import pyrebase
from front_end.Getters import get_database
from unittest.mock import patch, Mock
from front_end.Getters import get_firebase_connection

def test_init():
    pyrebase.initialize_app = Mock()
    db = get_database().db
    assert db is not None