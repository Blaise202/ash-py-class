account_active = True
has_2fa = True
# trial = True
# while trial:
print('Enter your credentials to login')
username = input('Username: ')
password = input('Password: ')
if username == 'admin' and password == 'secret':
    if account_active:
        print('Account is active')
        if has_2fa:
            print('Two-factor authentication is enabled')
            code = input('Enter the 2FA code: ')
            if code == '123456':
                print('2FA verification successful')
                print('Welcome to your account!')
            else:
                print('Invalid 2FA code')
        else:
            print('Two-factor authentication is not enabled')
    else:
        print('Account is inactive, please contact support')
    trial = False
else:
    print('Invalid username or password, please try again')