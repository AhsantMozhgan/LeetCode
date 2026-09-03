# https://leetcode.com/problems/search-a-2d-matrix

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Get Matrix Dimensions
        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize Search Range
        # Treat the entire matrix as one sorted array.
        left = 0
        right = rows * cols - 1

        # Binary Search
        while left <= right:

            # Find the middle position in the virtual 1D array.
            middle = (left + right) // 2

            # Convert the 1D index into a 2D row and column.
            row = middle // cols
            col = middle % cols

            # Target Found
            if matrix[row][col] == target:
                return True

            # Target Is Larger
            if matrix[row][col] < target:
                left = middle + 1

            # Target Is Smaller
            else:
                right = middle - 1

        # Target does not exist in the matrix.
        return False


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    print(solution.searchMatrix(matrix, 3))  # Output: True
    print(solution.searchMatrix(matrix, 13)) # Output: False

    
# The matrix is sorted row by row, and each row starts with a value greater than the previous row's last value. 
# Therefore, we can treat the matrix as one sorted one-dimensional array and perform binary search. 
# I use a virtual index from `0` to `rows * cols - 1`. For each middle index, I convert it back to a matrix position using `row = middle // cols` and `col = middle % cols`. 
# This lets me perform binary search without actually flattening the matrix. The time complexity is O(log(m × n)) and the space complexity is O(1).

# ---
# OR

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]:
#             return False
        
#         rows = len(matrix)
#         columns = len(matrix[0])
        
#         left, right = 0, rows * columns - 1
        
#         while left <= right:
#             mid = (left + right) // 2
#             # Convert mid index to 2D indices
#             mid_value = matrix[mid // columns][mid % columns]
            
#             if mid_value == target:
#                 return True
#             elif mid_value < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return False
