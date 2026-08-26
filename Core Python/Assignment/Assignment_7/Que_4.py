


for i in range(1, 6):

    # Print leading spaces
    for j in range(5 - i):
        print(" ", end=" ")

    # Print increasing numbers
    num = i
    for j in range(i):
        print(num, end=" ")
        num += 1

    # Print decreasing numbers
    num -= 2
    for j in range(i - 1):
        print(num, end=" ")
        num -= 1

    print()