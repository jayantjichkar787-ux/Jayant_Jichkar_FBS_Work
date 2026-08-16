# 2. Write a program to check if given number is Armstrong or not using recursive 
#    function. 


def armstrong(num, digits):
    if num == 0:
        return 0

    digit = num % 10

    return digit ** digits + armstrong(num // 10, digits)


n = int(input("Enter a number: "))

digits = len(str(n))

sum = armstrong(n, digits)

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# def armstrong(num, digits):
#     if(num == 0):
#         return 0

#     digits = num % 10 

#     return digits ** digits + armstrong(num // 10, digits)

# n = int(input('Enter Number : '))
# digits = len(str(n))
# sum = armstrong(n, digits)

# if(sum == n):
#     print('Armstrong Number..')
# else:
#     print('Not Armstrong Number..')