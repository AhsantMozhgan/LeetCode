# https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:

        # Store the number of valid solutions we find.
        result = 0

        # Keep track of columns that already contain a queen.
        columns = set()

        # Keep track of diagonals from top-left to bottom-right.
        diagonal_1 = set()

        # Keep track of diagonals from top-right to bottom-left.
        diagonal_2 = set()

        # Backtracking
        # row:
        # The row where we want to place the next queen.
        def backtrack(row):
            nonlocal result

            # Base Case
            # If we successfully placed a queen in every row, we found one valid solution.
            if row == n:
                result += 1
                return

            # Try Every Column
            for col in range(n):

                # Calculate the two diagonal identifiers.
                diagonal_1_id = row - col
                diagonal_2_id = row + col

                # If another queen already occupies this column or either diagonal, this position is invalid.
                if (col in columns or diagonal_1_id in diagonal_1 or diagonal_2_id in diagonal_2):
                    continue

                # Choose
                columns.add(col)
                diagonal_1.add(diagonal_1_id)
                diagonal_2.add(diagonal_2_id)

                # Move to the next row.
                backtrack(row + 1)

                # Backtrack
                # Remove the queen's restrictions so we can try another column.
                columns.remove(col)
                diagonal_1.remove(diagonal_1_id)
                diagonal_2.remove(diagonal_2_id)

        # Start from the first row.
        backtrack(0)

        # Return the number of valid solutions.
        return result

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    n = 4  # Example board size
    result = solution.totalNQueens(n)
    print(result)  # Expected output: 2 (There are two distinct solutions for 4-queens)
    

# I use backtracking and place exactly one queen in each row. For every row, I try every column and check whether that position is safe. 
# I use three sets to track occupied columns and the two types of diagonals. A cell belongs to one diagonal identified by `row - col` and the other identified by `row + col`. 
# If the position is safe, I place the queen, recursively move to the next row, and then remove the queen when backtracking. When `row == n`, all queens have been placed successfully, so I increment the solution count.

# ---
# # OR
# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         # Keep track of columns and diagonals where queens are placed
#         cols = set()  # Columns where queens are placed
#         pos_diag = set()  # Positive diagonals (row + col)
#         neg_diag = set()  # Negative diagonals (row - col)
        
#         def backtrack(row: int) -> int:
#             if row == n:
#                 return 1  # A valid solution is found
            
#             count = 0
#             for col in range(n):
#                 if col not in cols and (row + col) not in pos_diag and (row - col) not in neg_diag:
#                     # Place the queen
#                     cols.add(col)
#                     pos_diag.add(row + col)
#                     neg_diag.add(row - col)

#                     # Recur to place the next queen
#                     count += backtrack(row + 1)

#                     # Backtrack: remove the queen and try next position
#                     cols.remove(col)
#                     pos_diag.remove(row + col)
#                     neg_diag.remove(row - col)
                    
#             return count
        
#         return backtrack(0)
