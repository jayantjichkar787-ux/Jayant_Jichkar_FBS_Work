# WAP to find which number are divisible by 7 and multiple of 5.

start = int(input('Enter a Start Number :'))
end = int(input('Enter a End Number :'))
for i in range(start, end+1):
    if(i%7==0 and i%5==0):
        print(i)
        