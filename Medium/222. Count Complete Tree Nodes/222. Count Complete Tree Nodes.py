# https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if left_height == right_height:

            # Left subtree is perfect.
            # Number of nodes including the current root:
            # 2^left_height
            return ((2 ** left_height) + self.countNodes(root.right))

        else:

            # Right subtree is perfect.
            # Number of nodes including the current root:
            # 2^right_height
            return ((2 ** right_height) + self.countNodes(root.left))


    def get_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left

        return height

# Example Usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    solution = Solution()
    print(solution.countNodes(root))  # Output: 6

# Because the tree is complete, at every node either the left subtree or the right subtree is a perfect binary tree. 
# I calculate the height of the left and right subtrees. If the heights are equal, the left subtree is perfect, so I can count all of its nodes directly using `2^h - 1` and recursively process the right subtree. 
# Otherwise, the right subtree is perfect, so I count it directly and recursively process the left subtree.

# # ---
# OR
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:

#         # Base Case
#         # If the tree is empty, there are no nodes.
#         if not root:
#             return 0

#         # Find Left Height
#         # Follow the leftmost path.
#         left_height = 0
#         current_node = root

#         while current_node:
#             left_height += 1
#             current_node = current_node.left

#         # Find Right Height
#         # Follow the rightmost path.
#         right_height = 0
#         current_node = root

#         while current_node:
#             right_height += 1
#             current_node = current_node.right

#         # Perfect Binary Tree
#         # If both heights are equal, this subtree is perfect.
#         # Number of nodes:
#         # 2^height - 1
#         if left_height == right_height:
#             return (2 ** left_height) - 1

#         # Complete But Not Perfect
#         # Recursively count nodes in the left and right subtrees.
#         return (1 + self.countNodes(root.left) + self.countNodes(root.right))