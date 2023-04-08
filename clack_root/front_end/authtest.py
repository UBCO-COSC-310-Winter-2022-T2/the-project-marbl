import Auth

obj = Auth.FirebaseAuthentication()

response = obj.sign_in_with_email_and_password('123456@123456.com', '123456')
print(response,type(response))
if("error" in response):
    print(response['error']['message'])
else:
    print(response['localId'])
