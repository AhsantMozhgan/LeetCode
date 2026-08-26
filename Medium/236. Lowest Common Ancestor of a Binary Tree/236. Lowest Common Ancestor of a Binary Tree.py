# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Base Case
        # If the tree is empty, there is no common ancestor.
        if not root:
            return None

        # Found p or q
        # If the current node is either p or q, return it.
        if root == p or root == q:
            return root

        # Search Left Subtree
        left_result = self.lowestCommonAncestor(root.left, p, q)

        # Search Right Subtree
        right_result = self.lowestCommonAncestor(root.right, p, q)

        # p and q are on
        # different sides
        # If both sides found a node,
        # current root is their
        # lowest common ancestor.
        #
        if left_result and right_result:
            return root

        # Both are on one side
        # Return whichever side contains p or q.
        if left_result:
            return left_result

        return right_result

# Example Usage
if __name__ == "__main__":
    # Creating the sample tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    solution = Solution()
    lca = solution.lowestCommonAncestor(root, root.left, root.right)  # p = 5, q = 1
    print(lca.val)  # Output: 3
    
    lca = solution.lowestCommonAncestor(root, root.left, root.left.right.right)  # p = 5, q = 4
    print(lca.val)  # Output: 5

# I use DFS recursively. For each node, I search both the left and right subtrees for `p` and `q`. 
# If the current node is either `p` or `q`, I return it immediately. If both the left and right subtrees return a node, it means `p` and `q` are on different sides, 
# so the current node is their lowest common ancestor. If only one side returns a node, I pass that result upward
