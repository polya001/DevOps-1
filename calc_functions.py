
"""
Module with basic calc functions
"""

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "ERROR"
    return x / y

def power(x, y):
    """Exponentiation function"""
    return x ** y

def sqrt(x):
    """Square root function"""
    return x ** 0.5
