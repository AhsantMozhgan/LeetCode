# https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # Initialize previous node value as None and min_diff as infinity
        self.prev = None
        self.min_diff = float('inf')
        
        def in_order_traversal(node):
            if not node:
                return
            
            # Traverse the left subtree
            in_order_traversal(node.left)

            # Process the current node
            if self.prev is not None:
                # Calculate the difference with the previous node
                current_diff = node.val - self.prev
                self.min_diff = min(self.min_diff, current_diff)
            
            # Update previous node value
            self.prev = node.val
            
            # Traverse the right subtree
            in_order_traversal(node.right)
        
        # Start the in-order traversal
        in_order_traversal(root)
        
        return self.min_diff

# Example Usage
if __name__ == "__main__":
    # Constructing the example tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    solution = Solution()
    print(solution.getMinimumDifference(root))  # Output: 1


    
# Because this is a BST, I can use inorder traversal to visit the values in sorted order. The minimum absolute difference in a sorted sequence must occur between two adjacent values. 
# So during inorder traversal, I keep track of the previous value and compare it with the current value. 
# I update the minimum difference and then make the current value the previous value for the next node.
