def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    # Perform some calculations
    result = add_numbers(9, 7)
    print("Addition result:", result)

    result = subtract_numbers(8, 6)
    print("Subtraction result:", result)

    result = multiply_numbers(7, 5)
    print("Multiplication result:", result)

    try:
        result = divide_numbers(10, 3)
        print("Division result:", result)
    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
