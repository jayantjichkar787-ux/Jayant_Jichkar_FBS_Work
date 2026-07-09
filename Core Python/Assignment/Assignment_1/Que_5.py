#  WAP to enter P, T, R & calculate compound Interest

p = float(input('Enter Principal Amount : '))
r = float(input('Enter Rate of Interest : '))/100
t = float(input('Enter Time Period : '))
n = int(input('Enter Number of times Interest is compunded : '))

A  = p * (1 + r/n) ** (n * t)
ci = A - p

print(f'Total Amount with Compound Interest is {A}')
print(f' Compound Interest is {ci}')