# https://leetcode.com/problems/binary-tree-maximum-path-sum

# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Global Maximum
        # We store the best path sum found anywhere in the tree.
        # We use negative infinity because all node values can be negative.
        maximum_path_sum = float("-inf")

        # DFS
        # This function returns the maximum path sum that can be extended from the current node to its parent.
        def dfs(node):
            nonlocal maximum_path_sum

            # Base Case
            # An empty subtree contributes nothing.
            if not node:
                return 0

            # Left Gain
            # Find the maximum contribution we can get from the left subtree.
            # If it is negative, we ignore it.
            left_gain = max(dfs(node.left), 0)

            # Right Gain
            # Find the maximum contribution from the right subtree. Again, ignore negative values.
            right_gain = max(dfs(node.right), 0)

            # Path Through Current Node
            # A complete path can be:
            # Left → Current → Right
            # So calculate its total sum.
            current_path_sum = (left_gain + node.val+ right_gain)

            # Update Global Answer
            # This path might be the best path anywhere in the tree.
            maximum_path_sum = max(maximum_path_sum, current_path_sum)

            # Return To Parent
            # When returning to the parent, we can only choose ONE branch.
            # We cannot return both left and right branches because that would create a branching structure, not a single path.
            return node.val + max(left_gain,right_gain)


        # Start DFS from the root.
        dfs(root)

        return maximum_path_sum

# Example Usage
if __name__ == "__main__":
    # Construct the binary tree
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Create a solution instance
    solution = Solution()

    # Find the maximum path sum
    result = solution.maxPathSum(root)
    
    print(result)  # Output: 42


# I use DFS and calculate the maximum gain from each subtree. For every node, I ignore negative subtree contributions because they would only decrease the path sum. 
# There are two different values to consider. The maximum path passing through the current node can use both the left and right gains, so it is `left_gain + node.val + right_gain`. 
# But when returning a value to the parent, I can only use one side, so I return `node.val + max(left_gain, right_gain)`. 
# I keep a global maximum because the best path does not necessarily start at the root.
