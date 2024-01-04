#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit
last_digit = number % 10

# Print the initial part of the message
print("Last digit of", number, "is", last_digit, end=" ")

# Check the conditions for the last digit and print accordingly
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:  # last_digit is less than 6 and not 0
    print("and is less than 6 and not 0")
