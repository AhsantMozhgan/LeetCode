# https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # If the original list is empty, there is nothing to copy.
        if head is None:
            return None

        # This dictionary maps:
        # original node → copied node
        old_to_new = dict()

        # First Pass
        # Create a copy of every node.
        # At this point, we only copy the values. We do NOT connect next/random yet.
        current_node = head

        while current_node:

            old_to_new[current_node] = Node(current_node.val)
            current_node = current_node.next


        # Second Pass
        # Now connect the pointers. For every original node:
        # copy.next
        #     ↓
        # copied version of original.next
        # copy.random
        #     ↓
        # copied version of original.random
        current_node = head

        while current_node:
            copied_node = old_to_new[current_node]

            # Copy the next pointer.
            # If current_node.next is None, the result will also be None.
            copied_node.next = old_to_new.get(current_node.next)

            # Copy the random pointer.
            # Again, .get() returns None if the original random pointer is None.
            copied_node.random = old_to_new.get(current_node.random)

            current_node = current_node.next

        # Return Deep Copy
        # head is the original first node. old_to_new[head] is the copied first node.
        return old_to_new[head]


# I use a hash map to map each original node to its copied node. In the first pass, I create a copy of every node and store the mapping. 
# In the second pass, I connect the `next` and `random` pointers using the map. This works because by the second pass, every copied node already exists, 
# so any random pointer can be mapped directly to its corresponding copy

# ---
# The challenge is that a node’s random pointer can point to any node in the list — including itself or None — so I need a way to locate the corresponding copy of any original node in constant time.

# I use a dictionary that maps each original node to its newly created copy.

# In the first pass I walk the original list and create one new node for every original node, copying only its value. I store the original-to-copy mapping in the dictionary. 
# I deliberately leave the pointers unset at this stage, because the target nodes may not exist yet when I first encounter a pointer.

# In the second pass I walk the original list again. For each original node I retrieve its copy from the dictionary, then set  

# - `copied.next` to the copy of `original.next`, and  
# - `copied.random` to the copy of `original.random`.  

# I use a safe lookup so that if either original pointer is None, the corresponding copied pointer is also set to None.

# Finally I return the copy of the original head. This produces an entirely new list that preserves exactly the same next and random relationships.
