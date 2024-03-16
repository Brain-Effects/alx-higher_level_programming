#!/usr/bin/python3
def magic_string(history=[0]):
    history[0] += 1
    return "BestSchool, " * (history[0] - 1) + "BestSchool"
