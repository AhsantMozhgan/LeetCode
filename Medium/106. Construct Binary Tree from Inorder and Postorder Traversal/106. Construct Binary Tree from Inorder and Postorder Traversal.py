# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Map Inorder Values
        # Store the index of every value in the inorder array.
        # This allows O(1) lookup.
        inorder_index = {
            value: index
            for index, value in enumerate(inorder)
        }

        # Postorder Position
        # Start from the LAST element because postorder ends with Root.
        postorder_index = len(postorder) - 1

        # Build Tree
        def build(left_boundary, right_boundary):

            nonlocal postorder_index

            # Base Case
            # No values in this range.
            if left_boundary > right_boundary:
                return None

            # Get Root
            # The current last unused postorder value is the root.
            root_value = postorder[postorder_index]

            postorder_index -= 1

            # Create the root node.
            root = TreeNode(root_value)

            # Find Root in Inorder
            root_index = inorder_index[root_value]

            # Build Right Subtree
            # Postorder is:
            # Left → Right → Root
            #
            # When reading it backwards:
            # Root → Right → Left
            #
            # Therefore, build RIGHT first.
            root.right = build(root_index + 1, right_boundary)

            # Build Left Subtree

            # After building the right subtree, continue with the left subtree.
            root.left = build(left_boundary, root_index - 1)

            # Return the constructed subtree.
            return root

        # Start with the entire inorder array.
        return build(0, len(inorder) - 1)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    
    root = solution.buildTree(inorder, postorder)
    
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

    level_order_output = print_level_order(root)
    print(level_order_output)  # Output to verify the tree structure

# Postorder traversal is Left, Right, Root, so the last unused element is always the root of the current subtree. 
# I use a HashMap to store the positions of values in the inorder traversal. Once I find the root's position in inorder, everything to its left belongs to the left subtree and everything to its right belongs to the right subtree. 
# cause I process postorder from right to left, the order becomes Root, Right, Left. Therefore, I recursively build the right subtree first and then the left subtree. The time complexity is O(n), 
# because each node is processed once and inorder lookups are O(1) using the HashMap. The space complexity is O(n) for the HashMap and recursion in the worst case.

# ---

# OR      
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not postorder or not inorder:
#             return None
#         root = TreeNode(postorder[-1])
#         mid = inorder.index(postorder[-1])
#         root.left = self.buildTree(inorder[:mid], postorder[:mid])
#         root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
#         return root
