# 2. Write a program to find maximum and minimum element in a list. 

# for Maximum element

li = [45, 34, 55, 67, 78, 88, 35, 43]
max = li[0]
for ind in range(1, len(li)):
    if(li[ind] > max):
        max = li[ind]

print('Maximum elemet = ', max)

# For Minimum element


li = [45, 34, 55, 67, 78, 88, 35, 43]
min = li[0]
for ind in range(1, len(li)):
    if(li[ind] < min):
        min = li[ind]

print('Minimum elemet = ', min)
