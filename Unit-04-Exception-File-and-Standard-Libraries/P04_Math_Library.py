
import math

num = float(input("Enter a number: "))
n = int(input("Enter a number for factorial: "))

print("Square Root:", math.sqrt(num) if num >= 0 else "Not possible")
print("Power:", math.pow(num, 2))
print("Ceiling:", math.ceil(num))
print("Floor:", math.floor(num))

if n >= 0:
    print("Factorial:", math.factorial(n))
else:
    print("Factorial is not possible.")