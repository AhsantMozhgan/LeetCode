# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        result = []
        queue = [root]  # Start with the root in the queue
        left_to_right = True  # Flag for zigzag direction
        
        while queue:
            level_length = len(queue)
            level_values = []
            
            for _ in range(level_length):
                node = queue.pop(0)  # Remove the first node in the queue
                
                # Append the node's value to level_values based on direction
                level_values.append(node.val)
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the level_values list if the current level is right to left
            if not left_to_right:
                level_values.reverse()
            
            result.append(level_values)  # Add the current level list to the result
            left_to_right = not left_to_right  # Toggle the direction
        
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
    print(solution.zigzagLevelOrder(root))
    # Output: [[3], [20, 9], [15, 7]]


# I use BFS to process the tree level by level, just like a normal level-order traversal. For each level, I collect all node values from left to right. 
# I keep a boolean variable to track the direction. If the current level should be read from right to left, I reverse the level before adding it to the result. 
# After each level, I toggle the direction.
