# https://leetcode.com/problems/sort-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Base Case
        # An empty list or a list with one node is already sorted.
        if head is None or head.next is None:
            return head

        # Find Middle
        # Use slow and fast pointers to find the middle of the list.
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split The List
        # slow is the last node of the left half.
        right_head = slow.next

        # Disconnect the two halves.
        slow.next = None

        # Recursively Sort
        left = self.sortList(head)
        right = self.sortList(right_head)

        # Merge Sorted Lists
        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node makes merging easier because we do not need special handling for the head.
        dummy = ListNode(0)
        current = dummy

        # Compare nodes from both lists.
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next

            else:
                current.next = right
                right = right.next

            current = current.next

        # Attach whichever list still has remaining nodes.
        if left:
            current.next = left

        else:
            current.next = right

        return dummy.next

# Example usage
if __name__ == "__main__":
    # Create a linked list: 4 -> 2 -> 1 -> 3
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    solution = Solution()
    sorted_head = solution.sortList(head)

    # Function to print the sorted linked list
    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    print_list(sorted_head)  # Output: 1 -> 2 -> 3 -> 4 -> None

# I use merge sort because it works well with linked lists. First, I use slow and fast pointers to find the middle of the list and split it into two halves. Then I recursively sort both halves. Finally, I merge the two sorted linked lists by comparing their current nodes and connecting the smaller node to the result. I use a dummy node to simplify the merge logic. The time complexity is O(n log n), and the recursion uses O(log n) space.

# ---
# OR
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
        
#         # Helper function to split the linked list into two halves
#         def find_middle(start: ListNode, end: ListNode) -> ListNode:
#             slow = start
#             fast = start
            
#             while fast != end and fast.next != end:
#                 slow = slow.next
#                 fast = fast.next.next
            
#             return slow

#         # Helper function to merge two sorted linked lists
#         def merge(left: ListNode, right: ListNode) -> ListNode:
#             if not left:
#                 return right
#             if not right:
#                 return left
            
#             if left.val < right.val:
#                 left.next = merge(left.next, right)
#                 return left
#             else:
#                 right.next = merge(left, right.next)
#                 return right

#         # Split the list into two halves
#         middle = find_middle(head, None)
#         right_half = middle.next
#         middle.next = None  # Split the list into two parts
        
#         # Sort the two halves recursively
#         left_sorted = self.sortList(head)
#         right_sorted = self.sortList(right_half)

#         # Merge the sorted halves
#         return merge(left_sorted, right_sorted)
