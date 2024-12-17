# calcs.py

def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a, b):
    """Divides the first number by the second and returns the result.
    Raises an error if division by zero is attempted."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
