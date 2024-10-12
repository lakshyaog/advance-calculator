import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")

    while True:
        choice = input("Enter choice (1-9) or 'q' to quit: ")

        if choice == 'q':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '6', '7', '8', '9']:
            num1 = float(input("Enter first number: "))
            if choice in ['1', '2', '3', '4', '6']:
                num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"Square root of {num1} = {square_root(num1)}")
        elif choice == '6':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '7':
            print(f"Sine of {num1} degrees = {sine(num1)}")
        elif choice == '8':
            print(f"Cosine of {num1} degrees = {cosine(num1)}")
        elif choice == '9':
            print(f"Tangent of {num1} degrees = {tangent(num1)}")
        else:
            print("Invalid input!")

if __name__ == "__main__":
    calculator()
