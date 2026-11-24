
import sys

# Accept command-line arguments
if len(sys.argv) != 4:
    print("Usage: python program.py num1 num2 operator")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    op = sys.argv[3]

    # Perform arithmetic operation
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero.")
            sys.exit()
        result = a / b
    else:
        print("Invalid operator.")
        sys.exit()

    print("Result:", result)