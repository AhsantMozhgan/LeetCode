# https://leetcode.com/problems/minimum-path-sum

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # Get Grid Dimensions
        ROWS, COLS = len(grid), len(grid[0])

        # Create DP Table
        # dp[r][c] represents the minimum path sum from grid[r][c] to the bottom-right
        # corner.
        dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]

        # Set Base Case
        # This extra cell acts as a starting point for the bottom-right cell.
        dp[ROWS - 1][COLS] = 0

        # Fill DP Table
        # Move from bottom-right toward top-left.
        for r in range(ROWS - 1, -1, -1):

            for c in range(COLS - 1, -1, -1):

                # From the current cell, we can move:
                # Down  → dp[r + 1][c]
                # Right → dp[r][c + 1]
                dp[r][c] = (grid[r][c] + min( dp[r + 1][c], dp[r][c + 1]))

        # The top-left cell contains the minimum path sum.
        return dp[0][0]


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = solution.minPathSum(grid)
    print(result)  # Expected output: 7 (1 → 3 → 1 → 2)

# I use dynamic programming. I define `dp[r][c]` as the minimum path sum from the current cell to the bottom-right cell. 
# From each cell, I can only move down or right, so the best path is the current cell's value plus the minimum of the down and right paths. 
# I fill the DP table from bottom-right to top-left because the states I need have already been calculated. 
# I use an extra row and column initialized to infinity to represent invalid paths, and I set one virtual cell next to the bottom-right to zero 
# so the last cell can be calculated without special cases. The time complexity is O(mn) and the space complexity is O(mn).


# # ---
# # OR
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
#         dp[ROWS - 1][COLS] = 0

#         for r in range(ROWS - 1, -1, -1):
#             for c in range(COLS - 1, -1, -1):
#                 dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

#         return dp[0][0]


# # ---
# # OR

# from typing import List


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         # -----------------------
#         # Get Grid Dimensions
#         # -----------------------
#         #
#         rows = len(grid)
#         cols = len(grid[0])


#         # -----------------------
#         # Update First Row
#         # -----------------------
#         #
#         # In the first row, we can only
#         # move from left to right.
#         #
#         for col in range(1, cols):
#             grid[0][col] += grid[0][col - 1]


#         # -----------------------
#         # Update First Column
#         # -----------------------
#         #
#         # In the first column, we can only
#         # move from top to bottom.
#         #
#         for row in range(1, rows):
#             grid[row][0] += grid[row - 1][0]


#         # -----------------------
#         # Fill Remaining Cells
#         # -----------------------
#         #
#         # For every cell, we can arrive
#         # either from the top or from
#         # the left.
#         #
#         for row in range(1, rows):

#             for col in range(1, cols):

#                 # Choose the smaller path
#                 # from top or left.
#                 #
#                 grid[row][col] += min(
#                     grid[row - 1][col],
#                     grid[row][col - 1]
#                 )


#         # The bottom-right cell now contains
#         # the minimum path sum.
#         #
#         return grid[rows - 1][cols - 1]

# # I use dynamic programming on the grid. I define each cell as the minimum path sum needed to reach that cell from the top-left. 
# For every cell except the first row and first column, there are only two possible ways to arrive: from the top or from the left. 
# Therefore, I add the current cell's value to the minimum of those two paths. I handle the first row and first column separately because they have only one possible direction. 
# I can reuse the input grid as the DP table, which reduces the extra space to O(1). Finally, the bottom-right cell contains the minimum path sum.

# ---
# OR
# class Solution:
#     def minPathSum(self, grid: list) -> int:
#         if not grid or not grid[0]:
#             return 0
            
#         m, n = len(grid), len(grid[0])
#         dp = [[0] * n for _ in range(m)]  # Initialize the DP table

#         # Fill the DP table
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     dp[i][j] = grid[i][j]  # Starting point
#                 elif i == 0:
#                     dp[i][j] = dp[i][j - 1] + grid[i][j]  # First row (can only come from the left)
#                 elif j == 0:
#                     dp[i][j] = dp[i - 1][j] + grid[i][j]  # First column (can only come from above)
#                 else:
#                     dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]  # Min of coming from left or above

#         return dp[m - 1][n - 1]  # Return the value in the bottom-right corner


