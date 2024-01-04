#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Check if the number is positive, zero, or negative and
# print the result in a single line
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
