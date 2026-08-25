# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Previous Node
        # previous keeps track of the node that should come immediately after root.
        previous = None

        # Reverse Preorder

        # Normal preorder:
        # Root → Left → Right
        #
        # We process:
        # Right → Left → Root
        def flatten_tree(node):

            nonlocal previous

            # Base Case
            if not node:
                return

            # Process Right
            # Process the right subtree first.
            flatten_tree(node.right)

            # Process Left
            # Then process the left subtree.
            flatten_tree(node.left)

            # Connect Node
            # Put the current node before the previously processed node.
            node.right = previous

            # The flattened tree cannot have any left pointers.
            node.left = None

            # Current node becomes the new previous node.
            previous = node

        flatten_tree(root)

# Example Usage
if __name__ == "__main__":
    # Construct the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    # Create a solution instance
    solution = Solution()

    # Flatten the binary tree
    solution.flatten(root)

    # Print the flattened linked list
    current = root
    while current:
        print(current.val, end=" -> ")
        current = current.right


# The flattened tree must follow preorder traversal, which is Root, Left, Right. I process the tree in reverse preorder, which is Right, Left, Root. 
# I keep a `previous` pointer to the already flattened portion of the tree. For each node, I set its `right` pointer to `previous`, set its `left` pointer to `None`, 
# and then update `previous` to the current node. Each node is visited once, so the time complexity is O(n). The recursion stack uses O(h) space, where h is the height of the tree.


# ---
# # OR
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         if not root:
#             return

#         # Initialize a stack to store nodes
#         stack = [root]

#         # Previous node pointer
#         prev = None

#         while stack:
#             # Pop the top node from the stack
#             curr = stack.pop()

#             # If there is a previous node, we need to point it to the current one
#             if prev:
#                 prev.left = None  # Set left child to None
#                 prev.right = curr  # Link the previous node's right to current node

#             # Push the right and then left child onto the stack (right first so that left is processed next)
#             if curr.right:
#                 stack.append(curr.right)
#             if curr.left:
#                 stack.append(curr.left)

#             # Move the previous pointer to the current node
#             prev = curr