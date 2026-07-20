# WAP to check given number is Strong number.

num = int(input('Enter a number :'))
temp = num
sum = 1

while(temp>0):
    digit = temp % 10

    fact = 1
    for i in range(1, digit+1):
        fact = fact*i
        sum = sum + fact
        temp = temp//10

    if(sum == num):
        print('Strong number..')
    else:
        print("Not a Strong number..")

    