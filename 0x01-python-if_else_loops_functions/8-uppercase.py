#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:  # ASCII values for lowercase letters
            print(chr(ord(c) - 32), end='')  # Convert to uppercase
        else:
            print(c, end='')
    print('\n')
