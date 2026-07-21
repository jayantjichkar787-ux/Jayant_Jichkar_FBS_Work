# 1. Write a program to prompt user to enter userid and password. 
#    If Id andpassword is incorrect give him chance to re-enter the credentials. 
#    Let him try 3times. After that program to terminate.


for i in range(1, 4):
    UI = input('Enter userID : ')
    PW = input('Enter password : ')

    if(UI == 'Jayant31' and PW == 'jay@3110'):
        print('Login Succesfully...')
        break
    else:
        print('Invalid User id and password..')

if(UI != 'Jayant31' or PW != 'jay@3110'):
    print('Maximum Attempt reached...')