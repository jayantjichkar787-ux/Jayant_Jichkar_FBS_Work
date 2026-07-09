# WAP to enter P, T, R & calculate Simple Interest

p = int(input('Enter Principal Amount : '))
r = int(input('Enter Rate of Interest : '))
t = int(input('Enter Time Period : '))

si = (p*t*r)/100

print(f'Simple Interest is {si}')