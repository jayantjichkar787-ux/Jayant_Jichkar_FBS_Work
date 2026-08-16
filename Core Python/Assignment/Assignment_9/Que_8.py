# 8. Write a program to check whether a number is prime or not using recursion. 


def prime(n, i):
    if n <= 1:
        return False

    if i == n:
        return True

    if n % i == 0:
        return False

    return prime(n, i + 1)


n = int(input("Enter a number: "))

if prime(n, 2):
    print("Prime number")
else:
    print("Not a prime number")