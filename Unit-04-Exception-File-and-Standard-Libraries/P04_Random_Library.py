
import random

# Generate random integer
print("Random Number:", random.randint(1, 100))

# Select random element
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)
print("Random Element:", random.choice(numbers))

# Shuffle list elements
random.shuffle(numbers)

print("Shuffled List:", numbers)