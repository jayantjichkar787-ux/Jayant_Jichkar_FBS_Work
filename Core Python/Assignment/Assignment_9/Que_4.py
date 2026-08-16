# 4. Write a program to find sum of n numbers using recursion. 


def soS(n):
    if(n > 0):
        return n + soS(n-1)
    else:
        return 0

n = int(input('Enter Number : '))
res = soS(n)
print(res)