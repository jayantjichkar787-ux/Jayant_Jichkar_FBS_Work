# 7. WAP to check user entered correct Userid and Password

UI = input('Enter UserID : ')
PW = input('Enter Password : ')

if(UI == 'Jayant'):
    if(PW == '3110'):
        print('Login Successfully..')
    else:
        print('Incorrect Password')
else:
    print('Incorrect UserID.')