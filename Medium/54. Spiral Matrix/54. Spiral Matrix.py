# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # If the matrix is empty, return an empty list.
        if not matrix:
            return []

        # Define the four boundaries of the current layer of the matrix.
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        result = []


        # Continue while there is still a valid rectangle to process.
        while top <= bottom and left <= right:

            # 1. Move Left → Right
            # Read the top row.
            for column in range(left, right + 1):
                result.append(matrix[top][column])

            # The top row has been processed.
            top += 1


            # 2. Move Top → Bottom
            # Read the right column.
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])

            # The right column has been processed.
            right -= 1

            # 3. Move Right → Left
            # Read the bottom row from right to left. We only do this if there is still a bottom row.
            if top <= bottom:

                for column in range(right, left - 1, -1):
                    result.append(matrix[bottom][column])

                # The bottom row has been processed.
                bottom -= 1


            # 4. Move Bottom → Top
            # Read the left column from bottom to top. We only do this if there is still a left column.
            if left <= right:

                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])

                # The left column has been processed.
                left += 1

        return result


# I’d traverse the matrix layer by layer using four boundaries: top, bottom, left, and right. 
# These boundaries mark the still-unprocessed portion of the matrix.  

# For each layer I do four steps:  
# 1. Read the top row from left to right, then move the top boundary down.  
# 2. Read the right column from top to bottom, then move the right boundary left.  
# 3. If a row is still left, read the bottom row from right to left and move the bottom boundary up.  
# 4. If a column is still left, read the left column from bottom to top and move the left boundary right.  

# After those four directions the outer layer is finished, so I repeat the same process on the smaller inner rectangle.  
# The checks before the bottom-row and left-column steps prevent duplicates when only a single row or single column remains.  

# Every element is visited exactly once, so the time complexity is O(m × n) and the extra space is O(1) excluding the output list.