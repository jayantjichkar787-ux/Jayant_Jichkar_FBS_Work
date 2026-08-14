# 9. Write a program to check if entered number is a palindrome or not. 

def chkPallindrome():
    num = int(input('Enter a Number : '))
    temp = num
    rev = 0

    while(num != 0):
        d = num % 10
        rev = rev * 10 + d
        num = num // 10

    if(temp == rev):
        print('Number is Pallindrome...')
    else:
        print('Number is  Not Pallindrome...')
chkPallindrome()

# def palindrome():
#     num = int(input("Enter a number: "))
#     original = num
#     reverse = 0

#     while num != 0:
#         digit = num % 10
#         reverse = reverse * 10 + digit
#         num = num // 10

#     if original == reverse:
#         print("Palindrome number")
#     else:
#         print("Not a palindrome number"


# palindrome()