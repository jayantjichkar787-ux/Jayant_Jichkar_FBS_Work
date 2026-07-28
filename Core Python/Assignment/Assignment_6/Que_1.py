# Write a code to print pattern of Square of five "*"

for i in range(1, 6):
    for j in range(1, 6):
        if(i==1 or i==5 or j==1 or j==5):
            print('*', end = " ")
        else:
            print(" ", end = ' ')

    print()