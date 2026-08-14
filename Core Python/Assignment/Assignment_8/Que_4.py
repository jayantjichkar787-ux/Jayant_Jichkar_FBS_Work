# 4. Sum of all odd numbers between 1 to n 

def oddnumSum(num):
    sum = 0
    for i in range(1, n+1):
        if(i % 2 != 0):
            sum += i

    print('Sum of odd Number : ', sum)
n = int(input('Enter a NUMBER :'))
oddnumSum(n)
    