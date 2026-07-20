# WAP to print given number is prime number or not.

n = int(input('Enter Number :'))

if(n<=1):
    print('not Prime')
else:
    i = 2
    while(i<n):
        if(n % i == 0):
            print('not Prime')
            break
        i = i+1
    if(i == n):
        print('Prime Number.')    