#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:  # ASCII values for lowercase letters
            print("{}".format(chr(ord(c) - 32)), end='')  # Convert to uppercase
        else:
            print("{}".format(c), end='')
    print('\n')
