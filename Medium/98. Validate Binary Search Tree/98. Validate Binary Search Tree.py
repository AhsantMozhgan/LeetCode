# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
            
            val = node.val
            
            # Check the current node's value against the bounds
            if val <= low or val >= high:
                return False
            
            # Recursively validate the left and right subtrees
            return validate(node.left, low, val) and validate(node.right, val, high)

        # Start the validation from the root
        return validate(root)

# Example Usage
if __name__ == "__main__":
    # Constructing a valid BST
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    solution = Solution()
    print(solution.isValidBST(root))  # Output: True

    # Constructing an invalid BST
    invalid_root = TreeNode(5)
    invalid_root.left = TreeNode(1)
    invalid_root.right = TreeNode(4)
    invalid_root.right.left = TreeNode(3)
    invalid_root.right.right = TreeNode(6)

    print(solution.isValidBST(invalid_root))  # Output: False


    
# I validate the BST using a range for every node. Each node must be greater than the lower bound and smaller than the upper bound. 
# Initially, the root can have any value, so its range is negative infinity to positive infinity. When I move to the left subtree, the current node becomes the new upper bound. 
# When I move to the right subtree, the current node becomes the new lower bound. This ensures that every node respects the constraints of all its ancestors, not just its parent.

