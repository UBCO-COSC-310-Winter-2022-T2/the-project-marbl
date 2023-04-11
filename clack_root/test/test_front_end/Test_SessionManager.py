import pytest
from unittest.mock import patch
from front_end.SessionManager import SessionManager
from front_end.Session import Session
def test_signup():
    example_success_message = {'kind': 'identitytoolkit#VerifyPasswordResponse', 'localId': 'mB2KNYMvBzbwagrk35P9vUBTmPd2', 'email': 'passwordis123456@test.com', 'displayName': '', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg3YzFlN2Y4MDAzNGJiYzgxYjhmMmRiODM3OTIxZjRiZDI4N2YxZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY29zYzMxMC1tYXJibCIsImF1ZCI6ImNvc2MzMTAtbWFyYmwiLCJhdXRoX3RpbWUiOjE2ODA2NjI2MTcsInVzZXJfaWQiOiJtQjJLTllNdkJ6YndhZ3JrMzVQOXZVQlRtUGQyIiwic3ViIjoibUIyS05ZTXZCemJ3YWdyazM1UDl2VUJUbVBkMiIsImlhdCI6MTY4MDY2MjYxNywiZXhwIjoxNjgwNjY2MjE3LCJlbWFpbCI6InBhc3N3b3JkaXMxMjM0NTZAdGVzdC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsicGFzc3dvcmRpczEyMzQ1NkB0ZXN0LmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.H5GFuv8C1pWwmaVYBMa40mJV0Lu1ywNlde84MT92IhyQY4NuG05UA15lloUHOfQCsjV1j9urHqdt8eKztThquruHEBClcwaNr9ivGFhRCQ6wC6enR7hXl0QmbUsKcL2YYlnPCsEh0zFEqIuEoSkCNaf8Ioc9u6IwwCtVNL0mmf_I2QsVmSOK_mmh1D_2ZCSKVJIk9If3A-JsIWEgYj09joqyaOjeDg2vzHRlS1RV-2hSt5lOO2J9IgTfJNCwhxbxc9_K6CzV63QVo0YyHvCmyZdzxTgu_XSZythN4_g-TF2G-1v-n76iWwt0hry0f9_Th9mD3cYxLyuz6wdSenYO0g', 'registered': True, 'refreshToken': 'APJWN8dck6efr9CcYGnFpAWJbqwXbzFVBGCU1MKimqXHeu2VYmOlXQzOy5LHUTK9FHbtj3QBndZw3pMT1gNpAz1vc1hr7Nn3qP5Y_lNAub1NqJk1Jvd2kW3UML2oj4wEcBegbIk2gr_XuRMkl8pYdQvI1SrYO6vaD1rsJ_SulKpBWTDLp05xKE2HOkf0mbGak5tXEDhtfp2lDsJYYy41EoBQiSfgCk3SUQ', 'expiresIn': '3600'}
    example_fail_message = {'strerror':{'error': {'code': 400, 'errors': [{'domain': 'global', 'message': 'EMAIL_EXISTS', 'reason': 'invalid'}], 'message': 'EMAIL_EXISTS'}}}
    def mock_sign_in_with_email_and_password(email, password):
        if(email == 'valid@valid.com' and password == 'valid'):
            return example_success_message
        else:
            raise Exception(example_fail_message)
    
    with patch('front_end.SessionManager.auth') as mock_auth:
        mock_auth.sign_in_with_email_and_password = mock_sign_in_with_email_and_password
        SM = SessionManager()
        
        response1 = SM.sign_in_with_email_and_password('valid@valid.com', 'valid')
        assert type(response1) == Session

def test_register():
    example_success_message = {'kind': 'identitytoolkit#VerifyPasswordResponse', 'localId': 'mB2KNYMvBzbwagrk35P9vUBTmPd2', 'email': 'passwordis123456@test.com', 'displayName': '', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg3YzFlN2Y4MDAzNGJiYzgxYjhmMmRiODM3OTIxZjRiZDI4N2YxZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY29zYzMxMC1tYXJibCIsImF1ZCI6ImNvc2MzMTAtbWFyYmwiLCJhdXRoX3RpbWUiOjE2ODA2NjI2MTcsInVzZXJfaWQiOiJtQjJLTllNdkJ6YndhZ3JrMzVQOXZVQlRtUGQyIiwic3ViIjoibUIyS05ZTXZCemJ3YWdyazM1UDl2VUJUbVBkMiIsImlhdCI6MTY4MDY2MjYxNywiZXhwIjoxNjgwNjY2MjE3LCJlbWFpbCI6InBhc3N3b3JkaXMxMjM0NTZAdGVzdC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsicGFzc3dvcmRpczEyMzQ1NkB0ZXN0LmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.H5GFuv8C1pWwmaVYBMa40mJV0Lu1ywNlde84MT92IhyQY4NuG05UA15lloUHOfQCsjV1j9urHqdt8eKztThquruHEBClcwaNr9ivGFhRCQ6wC6enR7hXl0QmbUsKcL2YYlnPCsEh0zFEqIuEoSkCNaf8Ioc9u6IwwCtVNL0mmf_I2QsVmSOK_mmh1D_2ZCSKVJIk9If3A-JsIWEgYj09joqyaOjeDg2vzHRlS1RV-2hSt5lOO2J9IgTfJNCwhxbxc9_K6CzV63QVo0YyHvCmyZdzxTgu_XSZythN4_g-TF2G-1v-n76iWwt0hry0f9_Th9mD3cYxLyuz6wdSenYO0g', 'registered': True, 'refreshToken': 'APJWN8dck6efr9CcYGnFpAWJbqwXbzFVBGCU1MKimqXHeu2VYmOlXQzOy5LHUTK9FHbtj3QBndZw3pMT1gNpAz1vc1hr7Nn3qP5Y_lNAub1NqJk1Jvd2kW3UML2oj4wEcBegbIk2gr_XuRMkl8pYdQvI1SrYO6vaD1rsJ_SulKpBWTDLp05xKE2HOkf0mbGak5tXEDhtfp2lDsJYYy41EoBQiSfgCk3SUQ', 'expiresIn': '3600'}
    example_fail_message = {'strerror':{'error': {'code': 400, 'errors': [{'domain': 'global', 'message': 'EMAIL_EXISTS', 'reason': 'invalid'}], 'message': 'EMAIL_EXISTS'}}}
    def mock_create_account(email, password):
        if(email == 'valid@valid.com' and len(password) > 5): # firebase will not check validity of username, firstname, lastname
            return example_success_message
        else:
            class test():
                pass
            ret = test
            ret.strerror = example_fail_message
            return ret
    def mock_database(entry):
        if(entry == 'users'):
                return mock_database
        else:
            def set(entry):
                pass
            return set
    with patch('front_end.SessionManager.auth') as mock_auth:
        SM = SessionManager()
        def asd(username): pass
        def username_exists(username): return False
        SM.clear_user_data = asd
        SM.get_username_exists = username_exists
        with patch('front_end.SessionManager.database') as mock_database:
            mock_auth.create_user_with_email_and_password = mock_create_account
            mock_database.child = mock_database
            
            r1 = SM.create_account('valid@valid.com', 'valid1', 'validuser', 'validfirst', 'validlast') # success
            r2 = SM.create_account('invalid', 'invalid', 'validuser', 'validfirst', 'validlast') # fail (invalid email)
            r3 = SM.create_account('valid@valid.com', 'valid1','','','') # fail (blank fields)

            assert not "error" in r1
            assert r2 #my mock really sucks
            assert "error" in r3

def test_get_existing_session():
    example_success_message = {'kind': 'identitytoolkit#VerifyPasswordResponse', 'localId': 'mB2KNYMvBzbwagrk35P9vUBTmPd2', 'email': 'passwordis123456@test.com', 'displayName': '', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg3YzFlN2Y4MDAzNGJiYzgxYjhmMmRiODM3OTIxZjRiZDI4N2YxZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY29zYzMxMC1tYXJibCIsImF1ZCI6ImNvc2MzMTAtbWFyYmwiLCJhdXRoX3RpbWUiOjE2ODA2NjI2MTcsInVzZXJfaWQiOiJtQjJLTllNdkJ6YndhZ3JrMzVQOXZVQlRtUGQyIiwic3ViIjoibUIyS05ZTXZCemJ3YWdyazM1UDl2VUJUbVBkMiIsImlhdCI6MTY4MDY2MjYxNywiZXhwIjoxNjgwNjY2MjE3LCJlbWFpbCI6InBhc3N3b3JkaXMxMjM0NTZAdGVzdC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsicGFzc3dvcmRpczEyMzQ1NkB0ZXN0LmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.H5GFuv8C1pWwmaVYBMa40mJV0Lu1ywNlde84MT92IhyQY4NuG05UA15lloUHOfQCsjV1j9urHqdt8eKztThquruHEBClcwaNr9ivGFhRCQ6wC6enR7hXl0QmbUsKcL2YYlnPCsEh0zFEqIuEoSkCNaf8Ioc9u6IwwCtVNL0mmf_I2QsVmSOK_mmh1D_2ZCSKVJIk9If3A-JsIWEgYj09joqyaOjeDg2vzHRlS1RV-2hSt5lOO2J9IgTfJNCwhxbxc9_K6CzV63QVo0YyHvCmyZdzxTgu_XSZythN4_g-TF2G-1v-n76iWwt0hry0f9_Th9mD3cYxLyuz6wdSenYO0g', 'registered': True, 'refreshToken': 'APJWN8dck6efr9CcYGnFpAWJbqwXbzFVBGCU1MKimqXHeu2VYmOlXQzOy5LHUTK9FHbtj3QBndZw3pMT1gNpAz1vc1hr7Nn3qP5Y_lNAub1NqJk1Jvd2kW3UML2oj4wEcBegbIk2gr_XuRMkl8pYdQvI1SrYO6vaD1rsJ_SulKpBWTDLp05xKE2HOkf0mbGak5tXEDhtfp2lDsJYYy41EoBQiSfgCk3SUQ', 'expiresIn': '3600'}
    example_fail_message = {'error': {'code': 400, 'errors': [{'domain': 'global', 'message': 'EMAIL_EXISTS', 'reason': 'invalid'}], 'message': 'EMAIL_EXISTS'}}
    def mock_sign_in_with_email_and_password(email, password):
        if(email == 'valid@valid.com' and password == 'valid'):
            return example_success_message
        else:
            return example_fail_message
    
    with patch('front_end.SessionManager.auth') as mock_auth:
        mock_auth.sign_in_with_email_and_password = mock_sign_in_with_email_and_password
        SM = SessionManager()
        assert SM.get_existing_session() == None
        
        SM.sign_in_with_email_and_password('valid@valid.com', 'valid')
        assert SM.get_existing_session() != None

def test_forgot_password():
    example_success_message = {'localId': 'mB2KNYMvBzbwagrk35P9vUBTmPd2'}
    example_fail_message = {'error': {'code': 400, 'errors': [{'domain': 'global', 'message': 'EMAIL_EXISTS', 'reason': 'invalid'}], 'message': 'EMAIL_EXISTS'}}
    def mock_send_password_reset_email(email):
        if(email == 'valid@valid.com'):
            return example_success_message
        else:
            return example_fail_message
    
    SM = SessionManager()
    SM.forgot_password = mock_send_password_reset_email

    assert not "error" in SM.forgot_password('valid@valid.com')
    assert "error" in SM.forgot_password('invalid')