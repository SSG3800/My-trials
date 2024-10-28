username = input('Enter Your USER NAME = ')

if len(username) > 12:
    print('Your USER NAME is cannot be more than 12 characters')
elif not username.find(' ') == -1:
    print(' Your USER NAME cannot include spaces ')
elif not username.isdigit():
    print(' Your USER NAME cannot include Numbers ')
else:
    print(f'WELCOME {username}')