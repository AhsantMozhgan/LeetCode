# https://leetcode.com/problems/path-sum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # Base Case: Empty Tree
        # If there is no node, there is no path.
        if not root:
            return False

        # Check Leaf Node
        # If this is a leaf, check whether its value completes the target sum.
        if not root.left and not root.right:
            return root.val == targetSum

        # Remaining Sum
        # Subtract the current node's value from the target.
        remaining_sum = targetSum - root.val

        # Search Left or Right
        # We only need ONE valid path.
        return (self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(root.right, remaining_sum))


# Example Usage
if __name__ == "__main__":
    # Construct the binary tree
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    target_sum = 22

    # Create a solution instance
    solution = Solution()

    # Check if there is a path with sum equal to target_sum
    result = solution.hasPathSum(root, target_sum)
    
    print(result)  # Output: True
    
# I use DFS recursion. At each node, I subtract the node's value from the remaining target sum. 
# When I reach a leaf, I check whether the remaining sum equals the leaf's value. If the current node isn't a leaf, 
# I recursively search both the left and right subtrees and return true if either side contains a valid path. 
# The path must end at a leaf, so I specifically check the leaf condition instead of returning true as soon as the remaining sum becomes zero.
