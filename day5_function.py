# Day 5: Functions Practice

# 1️ Sum of numbers from 1 to n
def sum_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# 2 Prime check function
def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True

# 3️ Print all primes up to a given number
def print_primes(upto):
    print(f"Prime numbers from 1 to {upto}:")
    for i in range(2, upto+1):
        if is_prime(i):
            print(i, end=" ")
    print()  # new line after printing all primes

# 4️ Factorial function
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# -------------------------------
# Test the functions

# Sum numbers
num = int(input("Enter a number to sum: "))
print(f"Sum of numbers from 1 to {num}: {sum_numbers(num)}")
print("---------------------------")

# Prime check
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
print("---------------------------")

# Print all primes up to a number
num = int(input("Enter a number to print all primes up to it: "))
print_primes(num)
print("---------------------------")

# Factorial
num = int(input("Enter a number to calculate factorial: "))
print(f"{num}! = {factorial(num)}")
print("---------------------------")
