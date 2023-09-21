# factorial.py
import math

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return math.factorial(n)

if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    result = calculate_factorial(num)
    print(f"The factorial of {num} is {result}")
