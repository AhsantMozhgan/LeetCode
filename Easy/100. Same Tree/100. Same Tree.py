# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both Nodes Are Empty
        # If both nodes are None, both trees have no node at this position. Therefore, they are the same at this position.
        if p is None and q is None:
            return True

        # One Node Is Empty
        # If only one node is None, the tree structures are different.
        if p is None or q is None:
            return False

        # Compare Node Values
        # If both nodes exist but their values are different, the trees cannot be the same.
        if p.val != q.val:
            return False

        # Compare Left Subtrees
        # Recursively check whether the left subtrees are identical.
        left_is_same = self.isSameTree(p.left, q.left)

        # Compare Right Subtrees
        # Recursively check whether the right subtrees are identical.
        right_is_same = self.isSameTree(p.right, q.right)

        # Final Result
        # The current trees are the same only if both left and right subtrees are also the same.
        return left_is_same and right_is_same

# Example usage
if __name__ == "__main__":
    # Creating two identical trees
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    solution = Solution()
    result = solution.isSameTree(tree1, tree2)
    print(result)  # Output: True

    # Creating two non-identical trees
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(1)

    tree4 = TreeNode(1)
    tree4.left = TreeNode(1)
    tree4.right = TreeNode(2)

    result = solution.isSameTree(tree3, tree4)
    print(result)  # Output: False

# I compare the two trees recursively. If both nodes are `None`, they are identical at that position. 
# If only one is `None`, their structures are different. If both nodes exist, I first compare their values. 
# If the values match, I recursively compare their left and right subtrees. The two trees are the same only if the current values, left subtrees, and right subtrees all match. 
# The time complexity is O(n), where n is the number of nodes we compare, because each corresponding node is visited once. 
# The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.