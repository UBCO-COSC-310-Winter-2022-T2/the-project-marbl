from unittest.mock import MagicMock, patch
from front_end.Session import Session
from front_end.CommandInterface import CommandInterface

def test_login():
    # test that login returns the same instance
    with patch('front_end.CommandInterface.SM') as mock_SM:
        def mock_func(username, password):
            if(username == 'valid@valid.com' and password == 'valid'):
                return Session("idtoken", "expiry", "refreshtoken", True, "valid@valid.com")
            else:
                return 'invalid'
        
        mock_SM.sign_in_with_email_and_password = mock_func
        cmd = CommandInterface()
        r1 = cmd.Login('valid@valid.com', 'valid')
        r2 = cmd.Login('invalid', 'invalid')

        assert r1 and r1["success"] == True
        assert r1 and r1["session"] is not None

        assert r2 and r2["success"] == False
        assert r2 and r2["errorMsg"] is not None