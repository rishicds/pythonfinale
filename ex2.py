#calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Cannot divide by zero" if y == 0 else x / y

def square(x):
    return x ** 2

def power(x, y):
    return x ** y

#test1.py
import calculator

# Perform basic calculations
print("Addition: ", calculator.add(10, 5))
print("Subtraction: ", calculator.subtract(50, 20))
print("Multiplication: ", calculator.multiply(8, 7))
print("Division by Zero: ", calculator.divide(40, 0))


#test2.py
import calculator

# Test square and power functions
print("Square of 5: ", calculator.square(5))
print("2 raised to power 3: ", calculator.power(2, 3))
print("5 raised to power 2: ", calculator.power(5, 2))
