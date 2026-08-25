# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # Compare Two Sides
        # The tree is symmetric if its left subtree and right subtree are mirror images of each other.
        return self.isMirror(root.left, root.right)

    def isMirror(self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:

        # Both Nodes Are Empty
        # If both sides are None, they are symmetric at this position.
        if left_node is None and right_node is None:
            return True

        # One Node Is Empty
        # If only one side is None, the structure is not symmetric.
        if left_node is None or right_node is None:
            return False

        # Compare Values
        # Mirror nodes must have the same value.
        if left_node.val != right_node.val:
            return False

        # Compare Outer Children
        # The left child's LEFT side must match the right child's RIGHT side.
        outer_is_same = self.isMirror(left_node.left, right_node.right)

        # Compare Inner Children
        # The left child's RIGHT side must match the right child's LEFT side.
        inner_is_same = self.isMirror(left_node.right, right_node.left)

        # Final Result
        # Both the outer and inner sides must be mirror images.
        return outer_is_same and inner_is_same

# Example usage
if __name__ == "__main__":
    # Creating a symmetric tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    solution = Solution()
    result = solution.isSymmetric(root)
    print(result)  # Output: True

    # Creating a non-symmetric tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    result = solution.isSymmetric(root2)
    print(result)  # Output: False

# I treat the left and right subtrees as two trees that need to be mirror images. I recursively compare their corresponding nodes. 
# The values must be equal, but the children are compared in opposite directions: the left child of the left subtree is compared with the right child of the right subtree, 
# and the right child is compared with the left child. The time complexity is O(n) because each node is visited at most once. 
# The space complexity is O(h), where h is the height of the tree, because of the recursive call stack.

# ---
# # OR
# # Iterative Implementation

# from collections import deque

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:  # An empty tree is symmetric
#             return True
        
#         queue = deque([(root.left, root.right)])  # Start with the left and right children of the root
        
#         while queue:
#             t1, t2 = queue.popleft()  # Get the next pair of nodes to compare
            
#             if not t1 and not t2:  # Both nodes are None
#                 continue
#             if not t1 or not t2:  # One of the nodes is None, meaning it's not symmetric
#                 return False
#             if t1.val != t2.val:  # Values of the nodes are different
#                 return False
            
#             # Enqueue left and right children in a mirrored order
#             queue.append((t1.left, t2.right))
#             queue.append((t1.right, t2.left))
        
#         return True
