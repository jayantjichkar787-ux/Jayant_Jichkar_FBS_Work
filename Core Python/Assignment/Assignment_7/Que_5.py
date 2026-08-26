n = 5

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print("  ", end="")

    # Print first number
    print(1, end="")

    # Print middle spaces and last number
    if i > 1 and i < n:
        for j in range(2 * i - 3):
            print("  ", end="")
        print(i, end="")
    elif i == n:
        for j in range(2, n + 1):
            print(" " + str(j), end="")

    print()