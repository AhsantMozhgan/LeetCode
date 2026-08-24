# https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # -----------------------
        # Dummy Node
        # -----------------------
        #
        # Create a dummy node before
        # the actual head.
        #
        # This makes it easier to connect
        # the reversed groups together.
        #
        dummy = ListNode(0)
        dummy.next = head


        # -----------------------
        # Group Previous
        # -----------------------
        #
        # group_previous points to the node
        # immediately before the current group.
        #
        # Example:
        #
        # 0 → 1 → 2 → 3 → 4 → 5
        # ↑
        # group_previous
        #
        group_previous = dummy


        # -----------------------
        # Process Every Group
        # -----------------------
        #
        while True:

            # Find the kth node of the group.
            #
            # If there are fewer than k nodes,
            # we stop because the remaining nodes
            # should stay unchanged.
            #
            kth_node = group_previous

            for _ in range(k):

                kth_node = kth_node.next

                if kth_node is None:
                    return dummy.next


            # -----------------------
            # Save Group Boundaries
            # -----------------------
            #
            # group_next is the first node
            # after the current group.
            #
            # Example:
            #
            # 1 → 2 → 3 → 4
            #         ↑   ↑
            #       group   next
            #
            # group = 1,2,3
            # group_next = 4
            #
            group_next = kth_node.next


            # -----------------------
            # Reverse Current Group
            # -----------------------
            #
            # Reverse the nodes between
            # group_previous.next and kth_node.
            #
            previous_node = group_next
            current_node = group_previous.next

            while current_node != group_next:

                next_node = current_node.next

                current_node.next = previous_node

                previous_node = current_node
                current_node = next_node


            # -----------------------
            # Connect Previous Group
            # -----------------------
            #
            # Save the original first node.
            #
            # After reversal, this node becomes
            # the LAST node of the group.
            #
            group_first = group_previous.next


            # group_previous should now point
            # to the new first node of the group.
            #
            group_previous.next = kth_node


            # Move group_previous to the end
            # of the reversed group.
            #
            group_previous = group_first


# Example usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    k = 3
    new_head = solution.reverseKGroup(head, k)

    # Print the new list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next



# I use a dummy node to simplify reconnecting the reversed groups. For each group, I first check whether there are at least `k` nodes remaining. 
# If there are, I save the node after the group, reverse the `k` nodes in place, and reconnect the reversed group to the previous and next parts of the list. 
# If fewer than `k` nodes remain, I leave them unchanged.

# ---

# The goal is to reverse the linked list in groups of exactly k nodes. Any final group that contains fewer than k nodes must stay in its original order.

# I place a dummy node in front of the head so that every group has a well-defined predecessor. That makes reconnecting the first group straightforward, even when the original head itself gets reversed.

# A pointer called `group_previous` always sits on the node immediately before the current group.  

# Before I reverse a group I first walk a temporary pointer `k` steps ahead. If that walk hits None before finishing, there aren’t enough nodes left, so I stop and leave the remaining list untouched.

# When a complete group does exist, I record the node that comes right after the group (`group_next`). Then I reverse the k nodes using the classic three-pointer technique, initializing the “previous” pointer to `group_next`. 
# # That way, once the reversal finishes, the original first node of the group automatically points to the start of the next group.

# After the reversal, the node that used to be the k-th node is now the new head of the group, and the original first node is the new tail. I link `group_previous.next` to this new head, then advance `group_previous` to the original first node so it is ready for the next iteration.

# I keep repeating the process until fewer than k nodes remain, and finally return `dummy.next`.

# ---

# # OR
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         # Function to reverse a portion of the linked list
#         def reverse_linked_list(start: ListNode, end: ListNode) -> ListNode:
#             prev = None
#             current = start
#             while current != end:
#                 next_temp = current.next
#                 current.next = prev
#                 prev = current
#                 current = next_temp
#             return prev

#         # Count the length of the list
#         count = 0
#         current = head
#         while current:
#             count += 1
#             current = current.next
            
#         dummy = ListNode(0)
#         dummy.next = head
#         prev_end = dummy
        
#         # Reverse in k-group
#         while count >= k:
#             start = prev_end.next
#             end = start
            
#             # Move end pointer to k nodes ahead
#             for _ in range(k):
#                 end = end.next
            
#             # Reverse the current k-group
#             prev_end.next = reverse_linked_list(start, end)
            
#             # Connect the reversed part with the next nodes
#             start.next = end
            
#             # Move prev_end to the end of the reversed k-group
#             prev_end = start
            
#             # Decrease count by k
#             count -= k
        
#         return dummy.next  # Return the new head of the reversed list
