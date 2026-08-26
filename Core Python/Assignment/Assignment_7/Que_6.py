# WAP to print following pattern

for i in range(1, 6):

    for j in range(1, 6):

        if i == 1:              # First row
            print(j, end=" ")

        elif j == 1:            # First column
            print(i, end=" ")

        elif j == 6 - i:        # Diagonal
            print(5, end=" ")

        else:
            print(" ", end=" ")

    print()