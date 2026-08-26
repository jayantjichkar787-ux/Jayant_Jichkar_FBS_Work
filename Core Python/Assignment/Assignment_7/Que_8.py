


for i in range(1, 6):

    # Left side: 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")

    # Middle spaces
    for j in range(1, (5 - i) * 4 + 1):
        print(" ", end="")

    # Right side: i to 1
    if i != 5:
        for j in range(i, 0, -1):
            print(j, end=" ")
    else:
        for j in range(4, 0, -1):
            print(j, end=" ")

    print()

