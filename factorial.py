# Program to find the factorial of a number
# Compiled by Prof. Sujata Oak

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return 0  # Factorial does not exist for negative numbers
    elif n == 0 or n == 1:
        return 1  # Factorial of 0 or 1 is 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact

# Main code
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print("The factorial of", num, "is", factorial(num))

