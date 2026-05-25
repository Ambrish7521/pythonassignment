def solveNQueens(n):
    # This will store all valid solutions
    solutions = []

    # Sets to keep track of blocked columns and diagonals
    used_columns = set()
    used_diag1 = set()   # (row - col)
    used_diag2 = set()   # (row + col)

    # Create the chessboard filled with '#'
    board = [["#" for _ in range(n)] for _ in range(n)]

    # Backtracking function
    def placeQueen(row):
        # If would have placed queens in all rows, we found a solution
        if row == n:
            formatted_solution = ["".join(r) for r in board]
            solutions.append(formatted_solution)
            return

        # Try placing a queen in each column of the current row
        for col in range(n):

            # Check if the position is safe
            if (col in used_columns or
                (row - col) in used_diag1 or
                (row + col) in used_diag2):
                continue  # Not safe, try next column

            # Place a queen
            board[row][col] = "Q"
            used_columns.add(col)
            used_diag1.add(row - col)
            used_diag2.add(row + col)

            # Move to the next row
            placeQueen(row + 1)

            # Undo the move (Backtracking)
            board[row][col] = "#"
            used_columns.remove(col)
            used_diag1.remove(row - col)
            used_diag2.remove(row + col)

    # Start placing queens from row 0
    placeQueen(0)

    # Return the solutions and a count of them
    return solutions, len(solutions)


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter value of N: "))

solutions, count = solveNQueens(n)

print("\nAll Possible Solutions:\n")

for index, solution in enumerate(solutions, start=1):
    print(f"Solution {index}:")
    for row in solution:
        print(row)
    print()

print("Total Number of Solutions:", count)