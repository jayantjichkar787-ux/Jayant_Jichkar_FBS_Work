# 6. Write a program to find print the following Fibonacci series using 
# functions: 
# 1  1  2  3 5 8  n terms

def print_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    # Initialize the first two terms as specified (1 1 2 3...)
    a, b = 1, 1
    
    for i in range(n):
        print(a, end=" ")
        # Update the terms to calculate the next sequence number
        a, b = b, a + b
    print()  # Move to a new line after printing the series

# Get user input for the number of terms
terms = int(input("Enter the number of terms: "))
print_fibonacci(terms)
