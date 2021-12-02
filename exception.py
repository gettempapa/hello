import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Not a number")
    sys.exit(1)

try:
    print(f"{x} divided by {y} is equal to {x / y}")
except ZeroDivisionError:
    print("Cannot divide by zero")
    sys.exit(1)