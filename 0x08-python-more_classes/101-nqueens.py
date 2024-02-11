#!/usr/bin/python3
"""
This module contains a program that solves the N queens problem.

The N queens problem is the challenge of placing
N non-attacking queens on an N×N chessboard.

The program takes one command line argument, which is the number of queens N.
The program prints every possible solution to the problem, one per line,
in the format of a list of coordinates.
The program also checks the validity of the input and raises
appropriate exceptions if necessary.
"""


# Import the sys module
import sys


# Define a function to check if a position is safe for a queen
def is_safe(board, row, col):
    # Check the same row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    # Return true if no conflict is found
    return True


# Define a function to solve the N queens problem recursively
def solve(board, col):
    # Base case: if all queens are placed, print the solution
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return
    # Try placing a queen in each row of the current column
    for i in range(N):
        # Check if the position is safe
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1
            # Recur for the next column
            solve(board, col + 1)
            # Backtrack and remove the queen
            board[i][col] = 0


# Get the number of queens from the command line argument
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty board
board = [[0 for i in range(N)] for j in range(N)]

# Solve the N queens problem
solve(board, 0)
