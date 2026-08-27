# https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0  # Initialize count of nodes visited
        result = None  # To store the k-th smallest value
        
        def in_order(node):
            nonlocal count
            nonlocal result

            if not node:
                return
            
            # Traverse the left subtree
            in_order(node.left)
            
            # Increment the count and check if it's the k-th element
            count += 1
            if count == k:
                result = node.val
                return
            
            # Traverse the right subtree
            in_order(node.right)

        in_order(root)  # Start in-order traversal
        return result


# Example Usage
if __name__ == "__main__":
    # Constructing the example tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    solution = Solution()
    k = 3
    print(solution.kthSmallest(root, k))  # Output: 3

# Because this is a BST, an inorder traversal visits the nodes in sorted ascending order. I keep a counter that represents how many nodes I have visited. 
# Each time I visit a node, I increment the counter. When the counter reaches k, that node is the kth smallest element, so I return its value.
