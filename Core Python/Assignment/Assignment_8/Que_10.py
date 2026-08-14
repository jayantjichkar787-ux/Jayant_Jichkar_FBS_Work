# 10. Write a program to check if entered year is a leap year or not. 

def leapYear():
    year = int(input('Enter a Number of Year : '))
    
    if(year % 4 == 0):
        print('The Year is Leap Year...')
    else:
        print('The Year is not Leap Year...')
    
leapYear()    
