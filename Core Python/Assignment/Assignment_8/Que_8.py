# 8. Write a program find reverse of a number 

def reverseNum():
    num = int(input('Enter a Number : '))
    rev = 0
    while(num > 0):
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    print('Reverse of number is = ', rev) 
reverseNum()