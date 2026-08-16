# 3. Write a program to reverse a given number using recursive function. 


def reverseNum(n, rev):
    if(n == 0):
        return 0
    d = n % 10 
    rev = rev * 10 + n
    return reverseNum(n // 10, rev)

n = int(input('Enter Number : '))
res = reverseNum(n, 0)
print('Reverse of Number : ', res)

# def reverse_num(n, rev):
#     if n == 0:
#         return rev

#     digit = n % 10
#     rev = rev * 10 + digit

#     return reverse_num(n // 10, rev)


# n = int(input("Enter a number: "))

# result = reverse_num(n, 0)

# print("Reverse number =", result)

     

    