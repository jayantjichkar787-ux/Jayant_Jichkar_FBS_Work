# WAP to print all integer upto n which not divisible by 2 & 3.

n = int(input('Enter A Number :'))
i = 1
while(i<=n):
    if(i%2 !=0 and i%3 !=0):
        print(i)
    i = i+1
   