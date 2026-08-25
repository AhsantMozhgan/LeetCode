# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Map Inorder Values
        # Store the index of every value in the inorder array.
        # This allows us to find the root position in O(1).
        inorder_index = {
            value: index
            for index, value in enumerate(inorder)
        }

        # Preorder Position
        # preorder_index tells us which value should become the next root.
        preorder_index = 0

        # Build Tree
        def build(left_boundary, right_boundary):

            nonlocal preorder_index

            # Base Case
            # If the current inorder range is empty, there is no node to create.
            if left_boundary > right_boundary:
                return None

            # Get Root
            # The next value in preorder is the root of this subtree.
            root_value = preorder[preorder_index]

            preorder_index += 1

            # Create the root node.
            root = TreeNode(root_value)

            # Find Root Position
            # Find where the root appears in inorder.
            root_index = inorder_index[root_value]

            # Build Left Subtree
            # Values before root_index belong to the left subtree.
            root.left = build(left_boundary, root_index - 1)

            # Build Right Subtree
            # Values after root_index belong to the right subtree.
            root.right = build(root_index + 1, right_boundary)

            return root

        # Start with the entire inorder array.
        return build(0, len(inorder) - 1)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    root = solution.buildTree(preorder, inorder)
    
    # Function to print the tree in level order for verification
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
        
# Preorder tells us the root because the first unused element is always the root of the current subtree. 
# Inorder tells us how to split the tree because everything before the root belongs to the left subtree and everything after it belongs to the right subtree.
# I use a HashMap to store the index of every value in the inorder array, so I can find the root position in O(1). 
# I also keep a pointer into the preorder array so I can consume each root exactly once. 
# Then I recursively build the left subtree and the right subtree using the corresponding inorder boundaries.

# ---
# OR
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        # return root