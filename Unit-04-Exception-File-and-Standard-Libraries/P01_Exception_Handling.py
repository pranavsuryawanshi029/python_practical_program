
# Division with Exception Handling
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Division:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

else:
    print("Division successful.")

finally:
    print("Division operation completed.")

# Handle Invalid List Index
numbers = [10, 20, 30]

try:
    index = int(input("\nEnter list index: "))
    print("Element:", numbers[index])

except (ValueError, IndexError):
    print("Invalid index.")

# Raise Exception for Age
try:
    age = int(input("\nEnter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("You are eligible.")

except ValueError as e:
    print("Error:", e)

finally:
    print("Age checking completed.")