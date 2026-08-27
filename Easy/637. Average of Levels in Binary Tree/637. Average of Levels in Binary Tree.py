# https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []
        
        result = []
        queue = [root]  # Start with the root in the queue
        
        while queue:
            level_sum = 0  # Sum of values at the current level
            level_count = len(queue)  # Number of nodes at the current level
            
            for _ in range(level_count):
                node = queue.pop(0)  # Remove the first node in the queue
                level_sum += node.val  # Add the node's value to the level sum
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Compute the average and append to result
            average = level_sum / level_count
            result.append(average)
        
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
    print(solution.averageOfLevels(root))  # Output: [3.0, 14.5, 11.0]


# I use BFS to process the tree level by level. For each level, I first record its size so I know exactly which nodes belong to that level. 
# Then I remove each node from the queue, add its value to a running sum, and add its children to the queue for the next level. 
# After processing the entire level, I divide the sum by the level size and add the average to the result.
