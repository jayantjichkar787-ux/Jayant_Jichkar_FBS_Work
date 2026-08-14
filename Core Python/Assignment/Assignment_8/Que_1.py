# 1. Write a program to calculate area of rectangle

def areaRect(length, breath):
    area = length * breath

    print(f'Area of Rectangle of {length} and {breath} is {area}')

l = int(input('Enter length: '))
b = int(input('Enter Breath: '))
areaRect(l, b)