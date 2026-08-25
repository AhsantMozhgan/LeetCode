# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Base Case
        # If the current node is None, there is no tree here. Therefore, its depth is 0.
        if root is None:
            return 0

        # Find Left Depth
        # Recursively find the maximum depth of the left subtree.
        left_depth = self.maxDepth(root.left)

        # Find Right Depth
        # Recursively find the maximum depth of the right subtree.
        right_depth = self.maxDepth(root.right)

        # Calculate Current Depth
        # We take the deeper subtree and add 1 for the current node.
        return 1 + max(left_depth, right_depth)


# Example usage
if __name__ == "__main__":
    # Creating a sample binary tree:
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    depth = solution.maxDepth(root)
    print(depth)  # Output: 3


# I use recursion. For each node, I recursively calculate the maximum depth of its left and right subtrees. 
# The depth of the current node is one plus the larger of those two depths. If the node is `None`, I return 0 as the base case. 
# The time complexity is O(n) because we visit every node once. The space complexity is O(h), where h is the height of the tree, because of the recursive call stack. 
# In the worst case, when the tree is completely skewed, the space complexity is O(n).

# ---

# The maximum depth is the number of nodes on the longest path from the root down to a leaf.

# I solve it with a recursive depth-first search.  
# The base case is simple: if the node is None, its depth is zero.

# For any non-empty node I recursively compute the maximum depth of the left subtree and the maximum depth of the right subtree.  
# The depth of the current node is then one plus the larger of those two values, because the current node itself adds one level to the path.

# The recursion bottoms out at the leaves and the depth values are computed on the way back up, so it’s a classic bottom-up calculation.

# Time is O(n) because we visit every node once, and space is O(h) for the recursion stack, where h is the height of the tree (O(n) in the worst case of a skewed tree).