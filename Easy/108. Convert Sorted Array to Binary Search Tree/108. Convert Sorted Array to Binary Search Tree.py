# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # Build BST
        # Use the middle element as the root of the tree.
        def build_tree(left, right):

            # Base Case
            # If there are no elements in this range, return None.
            if left > right:
                return None

            # Find Middle
            # The middle element becomes the root of this subtree.
            middle = (left + right) // 2

            # Create Root
            root = TreeNode(nums[middle])

            # Build Left Subtree Elements before middle are smaller than the root.
            root.left = build_tree(left, middle - 1)

            # Build Right Subtree
            # Elements after middle are greater than the root.
            root.right = build_tree(middle + 1, right)
            return root

        # Start with the entire array.
        return build_tree(0, len(nums) - 1)

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    nums = [-10, -3, 0, 5, 9]
    root = solution.sortedArrayToBST(nums)

    # Function to print the tree in pre-order traversal for verification
    def print_tree(node):
        if not node:
            return
        print(node.val, end=' ')
        print_tree(node.left)
        print_tree(node.right)

    print_tree(root)  # Prints the tree in pre-order to show structure


# Because the array is sorted, I choose the middle element as the root. This guarantees that the left half contains smaller values and the right half contains larger values. 
# I then recursively build the left subtree from the left half and the right subtree from the right half. 
# I use left and right indices instead of creating new subarrays. When the range becomes empty, I return None. 
# Choosing the middle at every step keeps the resulting BST height-balanced.
