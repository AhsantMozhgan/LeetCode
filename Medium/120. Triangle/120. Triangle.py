# https://leetcode.com/problems/triangle

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # Start From Bottom Row
        # dp[col] represents the minimum path sum from the current position down to the bottom.
        dp = triangle[-1].copy()

        # Move Upward
        # Start from the second-to-last row and move toward the top.
        for row in range(len(triangle) - 2, -1, -1):

            # Visit every element in the current row.
            for col in range(len(triangle[row])):

                # From triangle[row][col], we can move to only two positions in the row below:
                # left  = dp[col]
                # right = dp[col + 1]
                dp[col] = (triangle[row][col] + min(dp[col], dp[col + 1]))

        # The top of the triangle now contains the minimum path sum.
        return dp[0]

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    result = solution.minimumTotal(triangle)
    print(result)  # Expected output: 11 (2 + 3 + 5 + 1)


# I use bottom-up dynamic programming. I start with the last row because each element in the last row is already the minimum path sum from that position to the bottom. 
# Then I move upward. For each position, I have only two possible positions in the row below. I choose the smaller one and add the current value. 
# So the recurrence is the current value plus the minimum of the two children. 
# I update the DP array in place to use O(n) extra space. At the end, `dp[0]` contains the minimum path sum from the top to the bottom.


# # ---
# # OR
# class Solution:
#     def minimumTotal(self, triangle: list) -> int:
#         # If the triangle is empty, return 0
#         if not triangle:
#             return 0
            
#         # Start from the second last row and go upwards
#         for row in range(len(triangle) - 2, -1, -1):
#             for col in range(len(triangle[row])):
#                 # Update the current position to be the minimum path sum of the two adjacent numbers in the next row
#                 triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

#         # The top element now contains the minimum path sum
#         return triangle[0][0]
