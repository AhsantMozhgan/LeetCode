# https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):

        # Stack
        # The stack stores nodes that we still need to visit.
        self.stack = []

        # Initialize Stack
        # Push the leftmost path starting from the root.
        self._push_left(root)

    # Push Left Path
    # Push the current node and all of its left descendants.
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    # next()
    # Return the next smallest value in the BST.
    def next(self) -> int:

        # The top of the stack is the next node in inorder.
        current_node = self.stack.pop()

        # Process Right Subtree
        # After visiting a node, inorder traversal moves to its right subtree.
        # We then push the entire left path of that subtree.
        self._push_left(current_node.right)

        # Return the current value.
        return current_node.val

    # hasNext()
    # If the stack is not empty, there is still a node to visit.
    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Example Usage
if __name__ == "__main__":
    # Creating the sample BST
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    iterator = BSTIterator(root)
    
    # Iterate through the BST
    while iterator.hasNext():
        print(iterator.next())


# Because this is a BST, an inorder traversal gives the values in ascending order. I use a stack to simulate inorder traversal iteratively. I initially push the entire left path from the root. For `next()`, I pop the top node, which is the next smallest value. Then I push the left path of its right subtree. `hasNext()` simply checks whether the stack is empty. 
# Why don't you store all values first? That would require O(n) initialization and storing all values. The stack-based approach lets the iterator produce values lazily, so initialization only processes the left path, and each node is processed once overall



# # OR
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.stack = []
#         while root:
#             self.stack.append(root)
#             root = root.left
        

#     def next(self) -> int:
#         res = self.stack.pop()
#         current = res.right
#         while current:
#             self.stack.append(current)
#             current = current.left
#         return res.val
        

#     def hasNext(self) -> bool:
#         return self.stack != []
