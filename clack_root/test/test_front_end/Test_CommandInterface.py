from unittest.mock import MagicMock, patch
from front_end.Session import Session
from front_end.Getters import getCommandInterface

def test_login():
    example_fail_message = {'error': {'code': 400, 'errors': [{'domain': 'global', 'message': 'EMAIL_EXISTS', 'reason': 'invalid'}], 'message': 'EMAIL_EXISTS'}}
    def mock_func(username, password):
        if(username == 'valid@valid.com' and password == 'valid'):
            return Session("idtoken", "expiry", "refreshtoken", True, "valid@valid.com")
        else:
            return example_fail_message
    
    cmd = getCommandInterface()
    cmd.SM.sign_in_with_email_and_password = mock_func
    r1 = cmd.Login('valid@valid.com', 'valid')
    r2 = cmd.Login('invalid', 'invalid')

    assert r1 and r1["success"] == True
    assert r1 and r1["session"] is not None

    assert r2 and r2["success"] == False
    assert r2 and r2["errorMsg"] is not None