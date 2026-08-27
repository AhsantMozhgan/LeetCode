# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        result = []
        queue = [root]  # Start with the root in the queue
        
        while queue:
            level_length = len(queue)
            level_values = []
            
            for _ in range(level_length):
                node = queue.pop(0)  # Remove the first node in the queue
                level_values.append(node.val)  # Add the node's value to the current level list
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)  # Add the current level list to the result

        return result

# Example Usage
if __name__ == "__main__":
    # Constructing the example tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.levelOrder(root))
    # Output: [[3], [9, 20], [15, 7]]

# I use BFS with a queue because I need to return the nodes level by level. For each iteration, I record the current queue size, which tells me how many nodes belong to the current level. 
# I process exactly those nodes, add their values to a temporary list, and add their children to the queue for the next level. 
# After processing the level, I add that list to the result.
