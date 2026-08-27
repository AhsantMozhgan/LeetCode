# https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        result = []
        queue = [root]  # Start with the root in the queue
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)  # Remove the first node in the queue
                
                # If it's the last node at the current level, add its value to result
                if i == level_length - 1:
                    result.append(node.val)

                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

# Example Usage
if __name__ == "__main__":
    # Constructing the example tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    solution = Solution()
    print(solution.rightSideView(root))  # Output: [1, 3, 4]

# I use BFS because the problem asks for the rightmost node at each level. I process the tree level by level using a queue. 
# For each level, I store its size so I know which node is the last one in that level. 
# When I reach the last node, I add its value to the result because that is the node visible from the right side.
