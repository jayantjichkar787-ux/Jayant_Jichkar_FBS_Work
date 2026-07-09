# WAP to  find the roots of a Quadratic equation

import math

a = float(input('Enter value of a :'))
b = float(input('Enter value of b :'))
c = float(input('Enter value of c :'))

d = b**2 - 4*a*c 
root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)

print(f'Root1 is {root1} & Root2 is {root2}.')