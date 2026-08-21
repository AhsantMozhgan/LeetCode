# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a temporary node before the actual result.
        # This makes it easier to build the merged linked list.
        dummy = ListNode(0)

        # current points to the last node in our result.
        current = dummy

        # Continue while both lists still have nodes.
        while list1 and list2:

            # Choose Smaller Node. Compare the current nodes.
            if list1.val <= list2.val:

                # Attach list1's node to the result.
                current.next = list1

                # Move list1 forward.
                list1 = list1.next

            else:

                # Attach list2's node to the result.
                current.next = list2

                # Move list2 forward.
                list2 = list2.next

            # Move current to the node we just added.
            current = current.next

        # Attach Remaining Nodes. 
        # At this point, one list is empty.
        # The other list is already sorted, so we can attach the entire remaining part.
        current.next = list1 or list2

        # dummy itself is not part of the answer.
        return dummy.next

# Example usage
if __name__ == "__main__":
    # Create the first linked list 1 -> 2 -> 4
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    
    # Create the second linked list 1 -> 3 -> 4
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    solution = Solution()
    merged_list = solution.mergeTwoLists(l1, l2)

    # Print the merged result
    while merged_list:
        print(merged_list.val, end=' -> ' if merged_list.next else '\n')
        merged_list = merged_list.next  # Move to the next node

# Both linked lists are already sorted, so I don't need to sort them again. I use two pointers, one for each list, and compare their current values. 
# I attach the smaller node to the result and move that pointer forward. 
# I continue until one list is empty, then attach the remaining part of the other list because it is already sorted.

# ---

# Both input lists are already sorted, so I can merge them with two pointers in linear time.  

# I start with a dummy node to simplify building the result, and a pointer called `current` that always sits on the last node of the merged list.

# While both lists still have nodes I compare their heads, attach the smaller one to `current.next`, and advance the pointer of the list I just took from. Then I move `current` forward to the newly attached node.

# As soon as one list becomes empty I no longer need to compare. The remaining nodes in the other list are already sorted and are all greater than or equal to everything I’ve already added, so I simply attach the entire leftover list in one step.

# The dummy node itself is only a placeholder; the real merged list starts at `dummy.next`, which is what I return.
