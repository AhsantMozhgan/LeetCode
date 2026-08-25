# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # Current Level
        # current points to the first node of the level we are currently processing.
        current = root

        # Process Each Level
        # Continue while the current level contains at least one node.
        while current:

            # Dummy Node
            # dummy is a temporary node that helps us build the next level.
            dummy = Node(0)

            # tail always points to the last node in the next level.
            tail = dummy

            # Traverse Current Level
            # current level is already connected using next pointers.
            while current:

                # Add Left Child
                # If current has a left child, add it to the next level.
                if current.left:
                    tail.next = current.left
                    tail = tail.next

                # Add Right Child
                # If current has a right child, add it after the previous child.

                if current.right:
                    tail.next = current.right
                    tail = tail.next

                # Move to the next node in the current level.
                current = current.next

            # Move To Next Level
            # dummy.next points to the first node of the next level.
            current = dummy.next

        # Return the original root.
        return root

# Example Usage
if __name__ == "__main__":
    # Creating a sample tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    
    solution = Solution()
    solution.connect(root)
    
    # Function to print the tree's next pointers
    def print_next_rights(node):
        while node:
            print(f'Node {node.val} -> Next {node.next.val if node.next else "None"}')
            node = node.next

    # Print next pointers for the first level
    print_next_rights(root)
    print_next_rights(root.left)


# I process the tree level by level using the existing `next` pointers. For each current level, I use a dummy node and a tail pointer to build the next level. 
# Whenever I find a left or right child, I append it to the next-level linked list. Then I move through the current level using `current.next`. 
# After finishing the level, `dummy.next` gives me the first node of the next level. Each node is visited exactly once, so the time complexity is O(n). 
# The extra space is O(1), excluding the output pointers, because I only use a dummy node and a few pointers.


# # ---
# OR
# BFS Implementation (Using a Queue)

# # Definition for a binary tree node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, next=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

# class Solution:
#     def connect(self, root: Node) -> Node:
#         if not root:
#             return root
        
#         from collections import deque
        
#         queue = deque([root])
        
#         while queue:
#             size = len(queue)  # Number of nodes at the current level
            
#             for i in range(size):
#                 node = queue.popleft()
                
#                 # Connect to the next node if it's not the last node of the current level
#                 if i < size - 1:
#                     node.next = queue[0]
                    
#                 # Add children to the queue
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
        
#         return root

# # Example Usage
# if __name__ == "__main__":
#     # Creating a sample tree
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(7)
    
#     solution = Solution()
#     solution.connect(root)
    
#     # Function to print the tree's next pointers
#     def print_next_rights(node):
#         while node:
#             print(f'Node {node.val} -> Next {node.next.val if node.next else "None"}')
#             node = node.next

#     # Print next pointers for the first level
#     print_next_rights(root)
#     print_next_rights(root.left)

# # ---
# # OR
# # DFS Implementation (Using Recursive Method)
# class Solution:
#     def connect(self, root: Node) -> Node:
#         if not root:
#             return root
        
#         # Start with the first level
#         def connect_next(parent: Node):
#             if not parent:
#                 return
            
#             # Connect children
#             if parent.left:
#                 if parent.right:
#                     parent.left.next = parent.right  # Connect left and right children
#                 else:
#                     parent.left.next = self.get_next(parent)  # Connect to next sibling if right child does not exist
#             if parent.right:
#                 parent.right.next = self.get_next(parent)  # Connect to next sibling
            
#             # Recur for the next level
#             connect_next(parent.right)  # Right child first
#             connect_next(parent.left)   # Then left child
            
#         # Helper function to find the next node at the same level
#         def get_next(node: Node) -> Node:
#             while node:
#                 if node.left:
#                     return node.left
#                 if node.right:
#                     return node.right
#                 node = node.next
#             return None
        
#         connect_next(root)
#         return root

# # Example Usage
# if __name__ == "__main__":
#     # Creating a sample tree
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(7)

#     solution = Solution()
#     solution.connect(root)

#     # Print next pointers for the first level
#     print_next_rights(root)
#     print_next_rights(root.left)

