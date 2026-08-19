# https://leetcode.com/problems/linked-list-cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Two Pointers: slow moves one step at a time. fast moves two steps at a time.
        # If there is a cycle, fast will eventually catch slow.
        slow = fast = head
        # OR
        # slow = head
        # fast = head

        # We can move fast two steps, so we need to make sure:
        # 1. fast is not None, 2. fast.next is not None
        while fast is not None and fast.next is not None:
        # OR
        # while fast and fast.next:

            # Move slow one step.
            slow = slow.next

            # Move fast two steps.
            fast = fast.next.next

            # Cycle Detected
            # If slow and fast point to the same node, they have met.
            # This can only happen because there is a cycle.
            if slow == fast:
                return True

        # No Cycle
        # If fast reaches None, the linked list ends. Therefore, there is no cycle.
        return False

# Example usage
if __name__ == "__main__":
    # Create a linked list with a cycle
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    # Build the cycle
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle

    solution = Solution()
    print(solution.hasCycle(node1))  # Output: True

    # Create a linked list without a cycle
    nodeA = ListNode(1)
    nodeB = ListNode(2)

    nodeA.next = nodeB

    print(solution.hasCycle(nodeA))  # Output: False

# I use Floyd's cycle detection algorithm with two pointers. The slow pointer moves one node at a time, while the fast pointer moves two nodes at a time. 
# If there is no cycle, the fast pointer eventually reaches the end of the list. 
# If there is a cycle, the fast pointer will eventually catch up with the slow pointer, so they will point to the same node.

# ---

# I use two pointers that move at different speeds — a slow pointer that advances one node at a time and a fast pointer that advances two nodes at a time.

# If the linked list has no cycle, the fast pointer will eventually reach the end (None or a node whose next is None), so I return false.

# If a cycle exists, both pointers will eventually enter it. Inside the cycle the fast pointer gains one node on the slow pointer with every iteration, 
# so it is guaranteed to catch up and land on the same node. When that happens I return true.

# I always check both `fast` and `fast.next` before advancing, because the fast pointer jumps two steps and I must avoid dereferencing a null node.

# This approach is more space-efficient than keeping a set of visited nodes — I only need the two pointers.


# ---
# OR
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:

#         seen = set()

#         while head:
#             seen.add(head)
#             head = head.next

#             if head in seen:
#                 return True
                
#         return False
