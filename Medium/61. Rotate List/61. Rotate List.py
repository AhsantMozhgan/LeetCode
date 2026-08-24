# https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        # -----------------------
        # Base Case
        # -----------------------
        #
        # If the list is empty,
        # has only one node,
        # or k is 0,
        # there is nothing to rotate.
        #
        if not head or not head.next or k == 0:
            return head


        # -----------------------
        # Find Length
        # -----------------------
        #
        # Traverse the list to find:
        #
        # 1. The length
        # 2. The last node
        #
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1


        # -----------------------
        # Reduce k
        # -----------------------
        #
        # Rotating a list by its length
        # gives us the original list.
        #
        # Example:
        #
        # length = 5
        # k = 7
        #
        # 7 % 5 = 2
        #
        k = k % length

        if k == 0:
            return head


        # -----------------------
        # Create a Circular List
        # -----------------------
        #
        # Connect the last node to the head.
        #
        # Before:
        #
        # 1 → 2 → 3 → 4 → 5
        #
        # After:
        #
        # 1 → 2 → 3 → 4 → 5
        # ↑             ↓
        # └─────────────┘
        #
        tail.next = head


        # -----------------------
        # Find New Tail
        # -----------------------
        #
        # The new tail is located
        # at:
        #
        # length - k - 1
        #
        # Example:
        #
        # length = 5
        # k = 2
        #
        # new tail position:
        #
        # 5 - 2 - 1 = 2
        #
        # Node at index 2 is 3.
        #
        new_tail = head

        for _ in range(length - k - 1):
            new_tail = new_tail.next


        # -----------------------
        # Find New Head
        # -----------------------
        #
        # The node after new_tail
        # becomes the new head.
        #
        # 1 → 2 → 3 → 4 → 5
        #         ↑   ↑
        #      new_tail new_head
        #
        new_head = new_tail.next


        # -----------------------
        # Break the Circle
        # -----------------------
        #
        # Cut the connection after
        # the new tail.
        #
        new_tail.next = None


        # -----------------------
        # Return Result
        # -----------------------
        #
        return new_head

# Example usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    k = 2
    new_head = solution.rotateRight(head, k)

    # Print the new linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# First, I find the length of the linked list and keep a pointer to the tail. Since rotating by the length gives the original list, I reduce `k` using `k % length`. 
# Then I connect the tail to the head to form a circular list. The new tail is located at `length - k - 1`, and the node after it becomes the new head. 
# Finally, I break the circle at the new tail and return the new head. The time complexity is O(n) because we traverse the list a constant number of times, and the extra space complexity is O(1).

# ---

# To rotate the list to the right by k positions I first walk the list once to find both its length and the tail node.  

# Because rotating by a multiple of the length leaves the list unchanged, I reduce k with `k % length`.  

# If the effective rotation is zero I simply return the original head.

# Otherwise I connect the tail back to the head, temporarily making the list circular. Now rotation becomes a question of where to break that circle.

# After a right rotation of k the new tail sits at index `length - k - 1`, and the node immediately after it becomes the new head.  

# I walk a pointer to that new-tail position, save its next node as the new head, and then set `new_tail.next = None` to break the circle.

# Finally I return the new head.

# The whole algorithm is O(n) time (a constant number of passes) and O(1) extra space.
