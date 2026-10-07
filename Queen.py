# 8-Queens Problem using Backtracking

N = 8

board = [-1] * N


def is_safe(row, col):
    for i in range(row):
        # Same column
        if board[i] == col:
            return False

        # Same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(row):
    # All queens are placed
    if row == N:
        return True

    # Try every column
    for col in range(N):

        if is_safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board():
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Solve the problem
if solve(0):
    print("Solution found:")
    print_board()
else:
    print("No solution exists.")
