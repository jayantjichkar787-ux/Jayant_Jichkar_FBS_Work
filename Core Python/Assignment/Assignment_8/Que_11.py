# 11. WAP to check if a given number is Armstrong number or not. 
#     For each task create separate functions. 

def armstrong():
    num = int(input("Enter a number: "))
    
    original = num
    sum = 0
    digits = len(str(num))

    while num != 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    if sum == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


armstrong()