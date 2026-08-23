# https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or m == n:
            return head

        # Dummy Node
        # Create a temporary node before the head.
        # This makes the code easier when left == 1.
        # dummy = ListNode(0)
        # dummy.next = head
        # OR
        dummy = ListNode(0,head)

        # Find Position Before Left
        # prev will point to the node
        # immediately before the section we want to reverse.
        #
        # Example:
        #
        # 1 → 2 → 3 → 4 → 5
        #     ↑
        #   left = 2
        #
        # prev should point to 1.
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # First Node of Reversed Part
        # current points to the first node inside the section that we want to reverse.
        #
        # Example:
        #
        # 1 → 2 → 3 → 4 → 5
        #     ↑
        #   current
        current = prev.next

        # Reverse the Section
        # We need to move every node after current to the front of the reversed section.
        for _ in range(right - left):

            # Save the node after current.
            # Example:
            #
            # 1 → 2 → 3 → 4 → 5
            #     ↑   ↑
            # current next_node
            next_node = current.next

            # Remove next_node from its current position and insert it immediately after prev.
            # Before:
            # prev → current → next_node
            #
            # After:
            # prev → next_node → current
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        # Return Result
        # dummy.next is the real head of the linked list.
        return dummy.next

# Example usage 
if __name__ == "__main__":
    # Creating a sample list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    m, n = 2, 4
    new_head = solution.reverseBetween(head, m, n)

    # Print the new list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# # I use a dummy node so that the logic also works when the reversal starts at the head. I first move a pointer to the node immediately before left. 
# Then I keep the first node of the reversal section fixed and repeatedly take the next node and insert it immediately after prev. 
# After right - left iterations, the selected section is reversed.

# ---

# I need to reverse only the portion of the linked list that lies between positions left and right, leaving everything else unchanged.

# I start with a dummy node that points to the head. This cleanly handles the edge case when left is 1, because the node just before the reversal section is then simply the dummy itself.

# I advance a pointer called `prev` until it sits on the node immediately before position left. Another pointer, `current`, points to the first node of the section that will be reversed.

# Instead of the classic full-list reversal, I repeatedly take the node that is right after `current` and move it to the front of the section — right after `prev`.  

# After one such move the local order changes from  

# `prev → current → next_node`  

# to  

# `prev → next_node → current`.

# I perform this operation exactly `right - left` times. Each iteration brings one more node to the front, so the selected segment is reversed in place. 
# The original first node of the segment stays at the back and remains correctly linked to the rest of the list through `current.next`.

# Finally I return `dummy.next`, which is the true head of the modified list.
