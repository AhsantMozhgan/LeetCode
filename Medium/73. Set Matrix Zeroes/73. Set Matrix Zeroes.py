# https://leetcode.com/problems/set-matrix-zeroes

# from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        columns = len(matrix[0])

        first_row_zero = False
        first_column_zero = False

        # Check if the first row contains a zero.
        for column in range(columns):
            if matrix[0][column] == 0:
                first_row_zero = True

        # Check if the first column contains a zero.
        for row in range(rows):
            if matrix[row][0] == 0:
                first_column_zero = True

        # Use the first row and first column as markers.
        for row in range(1, rows):
            for column in range(1, columns):

                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0

        # Set marked rows to zero.
        for row in range(1, rows):

            if matrix[row][0] == 0:
                for column in range(1, columns):
                    matrix[row][column] = 0

        # Set marked columns to zero.
        for column in range(1, columns):

            if matrix[0][column] == 0:
                for row in range(1, rows):
                    matrix[row][column] = 0

        # Handle the first row.
        if first_row_zero:
            for column in range(columns):
                matrix[0][column] = 0

        # Handle the first column.
        if first_column_zero:
            for row in range(rows):
                matrix[row][0] = 0


                
if __name__ == "__main__":
    solution = Solution()

    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    solution.setZeroes(matrix)
    print(matrix)  #[[1, 0, 1], [0, 0, 0], [1, 0, 1]]



# The goal is to set an entire row and column to zero whenever the original matrix contains a zero, while using only constant extra space.  

# Instead of allocating separate sets or arrays to remember which rows and columns need zeroing, I reuse the first row and first column of the matrix itself as marker storage.
#  Whenever I find a zero at `matrix[row][column]`, I set `matrix[row][0]` to zero to mark that row and `matrix[0][column]` to zero to mark that column.  

# Before I start writing those markers, I separately record whether the original first row or first column already contained a zero. 
# That step is necessary because I’m about to overwrite those cells, so I need to preserve their original zero status.  

# After the marking pass I scan the inner matrix again. If a cell’s row marker or column marker is zero, I set the cell itself to zero. 
# Finally I zero out the first row and first column according to the two flags I saved at the beginning.  

# The order is important: save the first-row and first-column state first, use them as markers next, apply the markers to the inner cells, and only zero the first row and column at the very end.  

# The whole algorithm runs in O(m × n) time and uses O(1) extra space.
