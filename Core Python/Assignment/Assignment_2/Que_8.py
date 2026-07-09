# WAP to find sum of three-digit number.

num = int(input('Enter Three-DigitNumber : '))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3 
print(f'Sum of Three-digit Number : {sum}')