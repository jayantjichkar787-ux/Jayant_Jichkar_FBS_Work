# WAP to print all the number in a range divisible by given number

start = int(input('Enter Start number :'))
end = int(input('Enter End number :'))
n = int(input('Enter a Divisor number '))

for i in range(start, end+1):
    if(i%n==0):
        print(i)