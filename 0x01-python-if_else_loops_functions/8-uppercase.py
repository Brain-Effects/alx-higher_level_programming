#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:  # ASCII values for lowercase letters
            result += chr(ord(c) - 32)  # Convert to uppercase
        else:
            result += c
    print("{}".format(result))
