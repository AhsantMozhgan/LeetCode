# https://leetcode.com/problems/unique-paths-ii

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # Get Grid Dimensions
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # Create DP Array
        # dp[col] represents the number of ways to reach the current cell in this column.
        dp = [0] * cols

        # There is one way to reach the starting position before processing the grid.
        dp[0] = 1

        # Process The Grid
        for row in range(rows):

            for col in range(cols):

                # Handle Obstacles
                # If this cell is blocked, there are zero ways to reach it.
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0

                    continue

                # Add Ways From The Left
                # dp[col] currently represents the number of ways from above. #
                # dp[col - 1] represents the number of ways from the left.
                if col > 0:
                    dp[col] += dp[col - 1]

        # The last cell contains the total number of unique paths.
        return dp[-1]

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result = solution.uniquePathsWithObstacles(obstacleGrid)
    print(result)  # Expected output: 2 (The paths are: down→down→right→right and right→down→down→right)

    
# I use dynamic programming. I define `dp[row][col]` as the number of unique paths to reach that cell. 
# Since we can only move down or right, every cell can be reached from the cell above or the cell to the left, so I add those two values. 
# If a cell contains an obstacle, I set its value to zero because no path can pass through it. 
# I can optimize the 2D DP to a one-dimensional array because each cell only depends on the current value from above and the previous value from the left. 
# The time complexity is O(rows × columns) and the space complexity is O(columns).


# # ---
# # OR
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
#         if not obstacleGrid or not obstacleGrid[0]:
#             return 0
        
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
        
#         # Create a 2D DP array initialized to 0
#         dp = [[0] * n for _ in range(m)]
        
#         # Start position
#         if obstacleGrid[0][0] == 0:
#             dp[0][0] = 1  # There's one way to reach the start if it's not an obstacle
        
#         # Fill the first row
#         for j in range(1, n):
#             if obstacleGrid[0][j] == 0:  # Only add path if there's no obstacle
#                 dp[0][j] = dp[0][j - 1]
        
#         # Fill the first column
#         for i in range(1, m):
#             if obstacleGrid[i][0] == 0:  # Only add path if there's no obstacle
#                 dp[i][0] = dp[i - 1][0]

#         # Fill the DP table
#         for i in range(1, m):
#             for j in range(1, n):
#                 if obstacleGrid[i][j] == 0:  # Only calculate if there's no obstacle
#                     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

#         return dp[m - 1][n - 1]  # Return the number of unique paths to the bottom-right corner
