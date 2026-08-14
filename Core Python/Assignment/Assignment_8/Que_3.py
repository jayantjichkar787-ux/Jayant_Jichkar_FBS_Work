# 3. Write a program to find sum of following series using functions : 
# a.  1+ 2 + 3 + 4+….. + n 
# b. 1!+ 2! + 3! + 4!+….. + n! 
# c. 1^1 + 2^2 + 3^3+ …… n^n


# a.  1+ 2 + 3 + 4+….. + n 

def addSeries():
    n = int(input('Enter a number : '))
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(f'Sum of Series {sum}')
   
addSeries()


# b. 1!+ 2! + 3! + 4!+….. + n! 

def addfactSeries():
    n = int(input('Enter a number : '))
    sum = 0

    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact = fact * j
        sum = sum + fact
    print(f'Sum of Series {sum}')
addfactSeries()


# c. 1^1 + 2^2 + 3^3+ …… n^n

def series():
    n = int(input("Enter N: "))

    sum = 0

    for i in range(1, n + 1):
        sum = sum + (i ** i)

    print("Sum =", sum)
series()