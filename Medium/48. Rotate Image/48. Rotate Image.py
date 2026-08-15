# https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Step 1: Transpose the matrix.
        # Swap matrix[row][column] with matrix[column][row].
        for row in range(n):
            for column in range(row + 1, n):
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column]
                )

        # Step 2: Reverse every row.
        for row in range(n):
            matrix[row].reverse()


# To rotate the matrix 90 degrees clockwise in place, I use two simple transformations: first transpose the matrix, then reverse every row.  

# I transpose by swapping `matrix[row][column]` with `matrix[column][row]` for every cell above the main diagonal. Starting the column index
#  at `row + 1` avoids touching the diagonal or swapping the same pair twice. After this step, the original rows have become columns.  

# Next I reverse each row. Once the matrix has been transposed, reversing the rows produces the final 90-degree clockwise rotation.  

# For example, after the transpose the original first column sits in the first row; reversing that row places those values in the correct clockwise order.  

# The whole algorithm runs in O(n²) time because every cell is processed a constant number of times, and it uses only O(1) extra space 
# since the rotation happens directly in the input matrix.