# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:

        # -----------------------
        # Dummy Node
        # -----------------------
        #
        # Create a dummy node before
        # the actual head.
        #
        # This makes it easier to remove
        # duplicate nodes at the beginning.
        #
        # Example:
        #
        # dummy → 1 → 2 → 2 → 3
        #
        dummy = ListNode(0)
        dummy.next = head


        # -----------------------
        # Two Pointers
        # -----------------------
        #
        # previous points to the last
        # node that we know should remain.
        #
        # current scans through the list.
        #
        previous = dummy
        current = head


        # -----------------------
        # Traverse the List
        # -----------------------
        #
        while current:

            # Check whether current starts
            # a group of duplicate values.
            #
            if current.next and current.val == current.next.val:

                # Store the duplicate value.
                duplicate_value = current.val


                # Skip every node having
                # the duplicate value.
                #
                while current and current.val == duplicate_value:
                    current = current.next


                # Connect previous directly
                # to the first non-duplicate node.
                #
                previous.next = current


            else:

                # Current value is unique,
                # so keep it.
                #
                previous = current
                current = current.next


        # -----------------------
        # Return Result
        # -----------------------
        #
        # dummy.next is the new head.
        #
        return dummy.next

# Example usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)

    solution = Solution()
    new_head = solution.deleteDuplicates(head)

    # Print the new linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


# Example usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)

    solution = Solution()
    new_head = solution.deleteDuplicates(head)

    # Print the new linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

#  Because the linked list is sorted, duplicate values are always adjacent. I use a dummy node and two pointers, `previous` and `current`. 
#  `previous` points to the last node that should remain in the result. 
#  When I find two consecutive nodes with the same value, I store that value and move `current` past all nodes with that value. 
#  Then I connect `previous.next` directly to `current`, removing the entire duplicate group. If the current value is unique, I move both pointers forward.

# ---

# Because the linked list is sorted, any duplicate values always sit next to each other, so I can process them as contiguous groups.

# I place a dummy node before the head so that duplicates appearing at the very beginning of the list can be removed without special-case handling.

# I keep two pointers:  
# - `previous` – the last node I know is unique and should stay in the result,  
# - `current` – the pointer that walks through the list.

# For each position of `current` I look ahead. If the next node has the same value, I record that value as a duplicate and keep advancing `current` until I have completely passed the whole group of matching values. Then I simply set `previous.next = current`, which skips the entire duplicate group (including its first occurrence).

# If the current value is unique I keep it by advancing both pointers.

# When I finish I return `dummy.next`, the new head of the cleaned-up list.
