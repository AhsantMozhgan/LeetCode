# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # -----------------------
        # Dummy Node
        # -----------------------
        #
        # Create a dummy node before
        # the actual head.
        #
        # Example:
        #
        # dummy → 1 → 2 → 3 → 4 → 5
        #
        # This makes it easier to handle
        # the case where we need to remove
        # the first node.
        #
        dummy = ListNode(0)
        dummy.next = head


        # -----------------------
        # Two Pointers
        # -----------------------
        #
        # Both pointers start at dummy.
        #
        fast = dummy
        slow = dummy


        # -----------------------
        # Create a Gap
        # -----------------------
        #
        # Move fast n + 1 steps forward.
        #
        # This creates a gap of n nodes
        # between fast and slow.
        #
        for _ in range(n + 1):
            fast = fast.next


        # -----------------------
        # Move Both Pointers
        # -----------------------
        #
        # Move both pointers together
        # until fast reaches the end.
        #
        # Because fast is n + 1 steps ahead,
        # slow will end up immediately before
        # the node we want to remove.
        #
        while fast:
            fast = fast.next
            slow = slow.next


        # -----------------------
        # Remove the Node
        # -----------------------
        #
        # slow is immediately before
        # the node we want to remove.
        #
        # Example:
        #
        # 1 → 2 → 3 → 4 → 5
        #         ↑
        #       slow
        #
        # slow.next is 4.
        #
        # Skip over 4:
        #
        # 3 → 5
        #
        slow.next = slow.next.next


        # -----------------------
        # Return Result
        # -----------------------
        #
        # dummy.next is the new head.
        #
        return dummy.next

# Example usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    n = 2
    new_head = solution.removeNthFromEnd(head, n)

    # Print the new linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next



# I use two pointers, `fast` and `slow`, with a dummy node before the head. I move `fast` `n + 1` steps ahead to create a fixed gap. Then I move both pointers together until `fast` reaches the end. At that point, `slow` is immediately before the node we need to remove, so I skip it using `slow.next = slow.next.next`. The dummy node also handles the case where the head itself needs to be removed.

# ---

# I need to remove the nth node from the end without first walking the list to find its length. I use two pointers — fast and slow — together with a dummy node placed before the head.

# Both pointers start at the dummy. I first advance the fast pointer n + 1 steps. That creates a fixed gap of n real nodes between fast and slow, and leaves slow in a position where it will eventually sit just before the node I want to delete.

# Then I move both pointers forward one step at a time until fast reaches None. Because the gap never changes, when fast hits the end, slow is exactly one node before the target.

# I remove the target by simply skipping it: `slow.next = slow.next.next`.  

# Finally I return `dummy.next`. The dummy itself is never part of the answer; it is only there to make the edge case clean. When n equals the length of the list (i.e., we must delete the original head), slow stays at the dummy, and the same assignment cleanly removes the head.

# ---
# OR

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         # Initialize a dummy node to handle the edge case of removing the head
#         dummy = ListNode(0)
#         dummy.next = head
#         first = dummy
#         second = dummy
        
#         # Move first pointer n+1 steps ahead
#         for _ in range(n + 1):
#             first = first.next
        
#         # Move both pointers until first reaches the end
#         while first:
#             first = first.next
#             second = second.next
        
#         # second.next is the node to be removed
#         second.next = second.next.next
        
#         return dummy.next  # Return the new head of the list
