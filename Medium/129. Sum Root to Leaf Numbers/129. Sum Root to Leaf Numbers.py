# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        # Base Case
        # If the tree is empty, there are no root-to-leaf numbers to add.
        if not root:
            return 0

        # DFS Function
        # current_number represents the number we have built from the root to the current node.
        def dfs(node, current_number):

            # Build Current Number
            # Add the current node's digit to the end of the number.
            # Example:
            # current_number = 12
            # node.val = 3
            # 12 * 10 + 3 = 123
            current_number = current_number * 10 + node.val

            # Leaf Node
            # If this node has no children, we have completed one root-to-leaf number.
            if not node.left and not node.right:
                return current_number

            # Search Left Subtree
            # If a left child exists, continue building the number.
            left_sum = 0

            if node.left:
                left_sum = dfs(node.left,current_number)

            # Search Right Subtree
            # If a right child exists, continue building the number.
            right_sum = 0

            if node.right:
                right_sum = dfs(node.right,current_number)

            # Add Both Sides
            # Return the sum of all numbers found in the left and right subtrees.
            return left_sum + right_sum

        # Start DFS from the root.
        # We initially have built the number 0.
        return dfs(root, 0)

# Example Usage
if __name__ == "__main__":
    # Construct the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create a solution instance
    solution = Solution()

    # Calculate the sum of all root-to-leaf numbers
    result = solution.sumNumbers(root)
    
    print(result)  # Output: 262

# # I use DFS and keep track of the number formed from the root to the current node. 
# At each node, I append its digit by multiplying the current number by 10 and adding the node's value. When I reach a leaf, the number is complete, so I return it. 
# Finally, I add the results from the left and right subtrees. The key observation is that when we move from a parent to a child, we can append the child's digit using `current_number * 10 + node.val`. 
# We only add the number when we reach a leaf, because only root-to-leaf paths count.
