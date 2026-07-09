# WAP to reverse three- digit number

num = int (input('Enter Three Digit number : '))

d3 = num % 10   
d2 = (num // 10) % 10 
d1 = num // 100

rev = d3*100 + d2*10 + d1

print(f'Reversed of three digit Number {rev}')