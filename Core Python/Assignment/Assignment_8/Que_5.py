# 5. Sum of all prime numbers between 1 to n 

def sum_of_primes(n):
    total_sum = 0
    for num in range(2, n + 1):
        # Check if num is prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total_sum += num
    return total_sum

# Example usage:
n = int(input("Enter the value of n: "))
print(f"The sum of prime numbers up to {n} is: {sum_of_primes(n)}")

        

        
        
        