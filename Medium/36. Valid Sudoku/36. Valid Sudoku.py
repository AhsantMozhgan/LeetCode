# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Create sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]       # rows[0] -> numbers seen in row 0
        columns = [set() for _ in range(9)]    # columns[0] -> numbers seen in column 0
        boxes = [set() for _ in range(9)]      # boxes[0] -> numbers seen in box 0


        # Check every cell in the board.
        for row in range(9):
            for column in range(9):

                current_value = board[row][column]

                # Ignore empty cells.
                if current_value == ".":
                    continue

                # Find the 3x3 Box. Each box is indexed by (row // 3) * 3 + (column // 3)
                box_index = (row // 3) * 3 + column // 3

                # Check for Duplicates
                if (
                    current_value in rows[row]
                    or current_value in columns[column]
                    or current_value in boxes[box_index]
                ):
                    return False

                # Add the number to all three corresponding sets.
                rows[row].add(current_value)
                columns[column].add(current_value)
                boxes[box_index].add(current_value)

        # No duplicates were found.
        return True



# I’d validate the board in a single pass using sets. I create nine sets for the rows, nine for the columns, and nine for the 3-by-3 boxes.
#  Each set simply records the digits I’ve already seen in that row, column, or box.  

# For every cell I skip it if it contains a ‘.’. Otherwise I compute which 3-by-3 box it belongs to with `(row // 3) * 3 + (column // 3)`.  

# Before adding the digit I check whether it already exists in its row set, its column set, or its box set. If it does, the board is invalid
#  and I return false immediately. If not, I add the digit to all three corresponding sets and continue.  

# If I finish the entire board without finding any duplicates, I return true.  

# Because a Sudoku board is fixed at 9 × 9, the solution is effectively constant time and constant space. More generally, for an n²-cell board it is O(n²) time and space.




# OR
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:

#         seen = set()

#         for r in range(9):
#             for c in range(9):
#                 num = board[r][c]

#                 if num == ".":
#                     continue

#                 row = ("row", r, num)
#                 col = ("col", c, num)
#                 box = ("box", r // 3, c // 3, num)

#                 if row in seen or col in seen or box in seen:
#                     return False

#                 seen.add(row)
#                 seen.add(col)
#                 seen.add(box)

#         return True
