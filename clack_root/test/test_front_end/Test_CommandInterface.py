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


def test_register():
    example_success_message = {'kind': 'identitytoolkit#VerifyPasswordResponse', 'localId': 'mB2KNYMvBzbwagrk35P9vUBTmPd2', 'email': 'passwordis123456@test.com', 'displayName': '', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg3YzFlN2Y4MDAzNGJiYzgxYjhmMmRiODM3OTIxZjRiZDI4N2YxZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY29zYzMxMC1tYXJibCIsImF1ZCI6ImNvc2MzMTAtbWFyYmwiLCJhdXRoX3RpbWUiOjE2ODA2NjI2MTcsInVzZXJfaWQiOiJtQjJLTllNdkJ6YndhZ3JrMzVQOXZVQlRtUGQyIiwic3ViIjoibUIyS05ZTXZCemJ3YWdyazM1UDl2VUJUbVBkMiIsImlhdCI6MTY4MDY2MjYxNywiZXhwIjoxNjgwNjY2MjE3LCJlbWFpbCI6InBhc3N3b3JkaXMxMjM0NTZAdGVzdC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsicGFzc3dvcmRpczEyMzQ1NkB0ZXN0LmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.H5GFuv8C1pWwmaVYBMa40mJV0Lu1ywNlde84MT92IhyQY4NuG05UA15lloUHOfQCsjV1j9urHqdt8eKztThquruHEBClcwaNr9ivGFhRCQ6wC6enR7hXl0QmbUsKcL2YYlnPCsEh0zFEqIuEoSkCNaf8Ioc9u6IwwCtVNL0mmf_I2QsVmSOK_mmh1D_2ZCSKVJIk9If3A-JsIWEgYj09joqyaOjeDg2vzHRlS1RV-2hSt5lOO2J9IgTfJNCwhxbxc9_K6CzV63QVo0YyHvCmyZdzxTgu_XSZythN4_g-TF2G-1v-n76iWwt0hry0f9_Th9mD3cYxLyuz6wdSenYO0g', 'registered': True, 'refreshToken': 'APJWN8dck6efr9CcYGnFpAWJbqwXbzFVBGCU1MKimqXHeu2VYmOlXQzOy5LHUTK9FHbtj3QBndZw3pMT1gNpAz1vc1hr7Nn3qP5Y_lNAub1NqJk1Jvd2kW3UML2oj4wEcBegbIk2gr_XuRMkl8pYdQvI1SrYO6vaD1rsJ_SulKpBWTDLp05xKE2HOkf0mbGak5tXEDhtfp2lDsJYYy41EoBQiSfgCk3SUQ', 'expiresIn': '3600'}
    example_fail_message = {'error': {'code': 400, 'errors': [{'domain': 'global', 'message': 'EMAIL_EXISTS', 'reason': 'invalid'}], 'message': 'EMAIL_EXISTS'}}
    def mock_func(email, password, username, first_name, last_name):
        if(email == 'valid@valid.com' and len(password) > 5): # firebase will not check validity of username, firstname, lastname
            return example_success_message
        else:
            return example_fail_message
    
    cmd = getCommandInterface()
    cmd.SM.create_user_with_email_and_password = mock_func
    r1 = cmd.createAccount('valid@valid.com', 'valid1', 'validuser', 'validfirst', 'validlast') # success
    r2 = cmd.createAccount('invalid', 'invalid', 'validuser', 'validfirst', 'validlast') # fail (invalid email)
    r3 = cmd.createAccount('valid@valid.com', 'valid1','','','') # fail (blank fields)
    r4 = cmd.createAccount('valid@valid.com', 'valid1','validuser','validfirst','') # fail (last name must be 1+ letters)
    r5 = cmd.createAccount('valid@valid.com', 'valid1','validuser','','validlast') # fail (first name must be 1+ letters)
    r6 = cmd.createAccount('valid@valid.com', 'valid1','a','validfirst','validlast') # fail (username must be 3+ letters)
    assert r1 and r1["success"] == True
    assert r2 and r2["success"] == False
    assert r3 and r3["success"] == False
    assert r4 and r4["success"] == False
    assert r5 and r5["success"] == False
    assert r6 and r6["success"] == False
