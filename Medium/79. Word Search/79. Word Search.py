# https://leetcode.com/problems/word-search

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Get the number of rows and columns in the board.
        rows = len(board)
        cols = len(board[0])

        # Backtracking / DFS
        # row:
        # Current row.
        # col:
        # Current column.
        # index:
        # The character of word we are currently looking for.
        def backtrack(row, col, index):

            # Word Found
            # If we matched every character in the word, the search is successful.
            if index == len(word):
                return True

            # Invalid Position
            # Stop if:
            # 1. We go outside the board.
            # 2. The current cell does not contain the character we need.
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
            ):
                return False

            # Mark As Visited
            # Temporarily change the current cell so we cannot use it again in this path.
            original_character = board[row][col]
            board[row][col] = "#"

            # Explore Four Directions
            found = (
                backtrack(row + 1, col, index + 1)
                or
                backtrack(row - 1, col, index + 1)
                or
                backtrack(row, col + 1, index + 1)
                or
                backtrack(row, col - 1, index + 1)
            )

            # Backtrack
            # Restore the original character so this cell can be used in another path.
            board[row][col] = original_character
            return found

        # Try Every Cell
        # The word can start from any cell in the board
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True

        # No valid path was found.
        return False

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"
    result = solution.exist(board, word)
    print(result)  # Expected output: True


# I use DFS with backtracking. I try starting the word from every cell in the board. At each step, I check whether the current cell contains the character I need. 
# If it does, I temporarily mark the cell as visited, then search in the four neighboring directions for the next character. 
# After exploring those directions, I restore the original character so the cell can be used by another path. If we match all characters in the word, we return true.


# # ---
# # OR        

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board or not board[0] or not word:
#             return False
        
#         rows, cols = len(board), len(board[0])

#         def dfs(r: int, c: int, index: int) -> bool:
#             # Base case: If all characters are found
#             if index == len(word):
#                 return True
            
#             # Out of bounds or mismatch or already visited
#             if (r < 0 or r >= rows or 
#                 c < 0 or c >= cols or 
#                 board[r][c] != word[index]):
#                 return False
            
#             # Mark the cell as visited
#             temp = board[r][c]
#             board[r][c] = '#'

#             # Explore all 4 directions
#             found = (dfs(r + 1, c, index + 1) or  # down
#                      dfs(r - 1, c, index + 1) or  # up
#                      dfs(r, c + 1, index + 1) or  # right
#                      dfs(r, c - 1, index + 1))    # left

#             # Restore the cell's value after the search
#             board[r][c] = temp
#             return found

#         # Start DFS from every cell in the board
#         for i in range(rows):
#             for j in range(cols):
#                 if board[i][j] == word[0]:  # Start DFS if the first letter matches
#                     if dfs(i, j, 0):
#                         return True

#         return False
