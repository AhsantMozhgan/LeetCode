# https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # If the current node is None, there is nothing to invert.
        if root is None:
            return None

        # Swap Left and Right
        # Exchange the left and right children of the current node.
        root.left, root.right = root.right, root.left

        # Invert Left Subtree
        # Recursively invert the new left subtree.
        self.invertTree(root.left)

        # Invert Right Subtree
        # Recursively invert the new right subtree.
        self.invertTree(root.right)

        # Return Root
        # The tree has been inverted in-place, so return the root.
        return root

# Example usage
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    solution = Solution()
    inverted_root = solution.invertTree(root)

    # Function to print the tree level-wise for verification
    def print_level_order(node):
        if not node:
            return "[]"
        result, current_level = [], [node]
        while current_level:
            next_level = []
            current_values = []
            for n in current_level:
                if n:
                    current_values.append(n.val)
                    next_level.append(n.left)
                    next_level.append(n.right)
                else:
                    current_values.append(None)

            result.append(current_values)
            current_level = next_level

        # Remove trailing levels of None values
        while result and all(val is None for val in result[-1]):
            result.pop()

        return result

    print(print_level_order(inverted_root))  
    # Output to verify the structure of the inverted tree


# I use recursion to invert the tree in place. For each node, I swap its left and right children, then recursively invert the new left and right subtrees. 
# If the current node is `None`, I return `None`. Finally, I return the root because the tree has been modified in place. 
# e time complexity is O(n) because every node is visited once. The space complexity is O(h), where h is the height of the tree, because of the recursive call stack.


# # ---
# # OR
# # Implementation (Iterative Approach)
# from collections import deque

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if root is None:
#             return None
        
#         queue = deque([root])
        
#         while queue:
#             node = queue.popleft()  # Get the next node
#             # Swap the children
#             node.left, node.right = node.right, node.left
            
#             # Add children to the queue if they are not null
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#         return root
