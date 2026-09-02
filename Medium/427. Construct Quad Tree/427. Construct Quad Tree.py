# https://leetcode.com/problems/construct-quad-tree

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        # Build Quad Tree
        # row_start:
        # Starting row of the region.
        # col_start:
        # Starting column of the region.
        # size:
        # Size of the square region.
        def build(row_start, col_start, size):

            # Check If Region Is Uniform
            # Assume the region is uniform until we find a different value.
            first_value = grid[row_start][col_start]
            is_uniform = True

            for row in range(row_start, row_start + size):
                for col in range(col_start, col_start + size):
                    if grid[row][col] != first_value:
                        is_uniform = False
                        break

                if not is_uniform:
                    break

            # Create Leaf Node
            # If every cell has the same value, we do not need to divide the region anymore.
            if is_uniform:
                return Node(first_value, True,  None, None, None, None)

            # Divide Into Four Parts
            # The region is not uniform, so divide it into four equal quadrants.
            half = size // 2

            # Top-left quadrant.
            top_left = build(row_start, col_start, half)

            # Top-right quadrant.
            top_right = build(row_start, col_start + half, half)

            # Bottom-left quadrant.
            bottom_left = build(row_start + half, col_start, half)

            # Bottom-right quadrant.
            bottom_right = build(row_start + half, col_start + half, half)

            # Create Internal Node
            # This node is not a leaf. Its four children represent the four quadrants.
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)

        # Start with the entire grid.
        return build(0, 0, len(grid))

        
# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]
    root = solution.construct(grid)

    # Function to print the quadtree in a structured format (for verification)
    def print_quadtree(node):
        if node.isLeaf:
            print(f"Leaf(val={node.val})")
        else:
            print("Internal Node:")
            print("Top Left:")
            print_quadtree(node.topLeft)
            print("Top Right:")
            print_quadtree(node.topRight)
            print("Bottom Left:")
            print_quadtree(node.bottomLeft)
            print("Bottom Right:")
            print_quadtree(node.bottomRight)

    print_quadtree(root)
        


# I use recursion with divide and conquer. For each square region, I first check whether all cells have the same value. 
# If they do, I create a leaf node containing that value. If the region contains different values, I divide it into four equal quadrants: top-left, top-right, bottom-left, and bottom-right. 
# I recursively construct a Quad Tree for each quadrant and attach them to a non-leaf parent node. I use row, column, and size indices instead of creating new sub-grids.

# ---
# OR
# # Definition for a quadtree node.
# class Node:
#     def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

# class Solution:
#     def construct(self, grid: List[List[int]]) -> Node:
#         def is_uniform(row1: int, col1: int, row2: int, col2: int) -> bool:
#             first_value = grid[row1][col1]
#             for i in range(row1, row2):
#                 for j in range(col1, col2):
#                     if grid[i][j] != first_value:
#                         return False
#             return True
        
#         def build_tree(row1: int, col1: int, row2: int, col2: int) -> Node:
#             # Check if the region is uniform
#             if is_uniform(row1, col1, row2, col2):
#                 return Node(val=grid[row1][col1], isLeaf=True)
            
#             # Calculate the midpoints
#             mid_row = (row1 + row2) // 2
#             mid_col = (col1 + col2) // 2
            
#             # Construct the four quadrants
#             topLeft = build_tree(row1, col1, mid_row, mid_col)
#             topRight = build_tree(row1, mid_col, mid_row, col2)
#             bottomLeft = build_tree(mid_row, col1, row2, mid_col)
#             bottomRight = build_tree(mid_row, mid_col, row2, col2)
            
#             return Node(val=True, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)

#         return build_tree(0, 0, len(grid), len(grid[0]))
