# 4. WAP to input all sides of Triangle and check triangle is valid or not 

a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))

if(a+b>c and a+c>b and b+c>a):
    print('Triangle is Valid')
else:
    print('Triangle is Invalid')
