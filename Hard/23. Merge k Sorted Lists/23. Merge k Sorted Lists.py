# https://leetcode.com/problems/merge-k-sorted-lists

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Handle Empty Input
        # If there are no linked lists, there is nothing to merge.
        if not lists:
            return None

        # Divide and Conquer
        # Recursively merge the lists between left and right.
        def merge_range(left, right):

            # Base Case
            # Only one list remains.
            if left == right:
                return lists[left]

            # Find Middle
            middle = (left + right) // 2

            # Merge Left Half
            left_list = merge_range(left, middle)

            # Merge Right Half
            right_list = merge_range(middle + 1, right)

            # Merge Two Sorted Lists
            return merge_two_lists(left_list, right_list)

        # Merge Two Lists
        def merge_two_lists(left, right):

            # Dummy node makes it easier to build the resulting list.
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

            # Attach the remaining nodes.
            if left:
                current.next = left

            else:
                current.next = right

            return dummy.next

        # Start with all k lists.
        return merge_range(0, len(lists) - 1)


# Example usage
if __name__ == "__main__":
    # Create example linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]

    solution = Solution()
    merged_head = solution.mergeKLists(lists)

    # Function to print the merged linked list
    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    print_list(merged_head)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

# I use divide and conquer to merge the k sorted linked lists efficiently. I recursively divide the list of linked lists into two halves until only one list remains. Then I merge the two sorted halves using the standard two-pointer merge technique. This gives us O(n log k) time, where n is the total number of nodes and k is the number of lists. The merge itself uses O(1) extra space because I reuse the existing nodes, while the recursion uses O(log k) space.

# ---
# OR
# import heapq

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         # A min-heap to keep track of the smallest head nodes
#         min_heap = []
        
#         # Initialize the heap with the head node of each list
#         for l in lists:
#             if l:  # Ensure that the list is not empty
#                 heapq.heappush(min_heap, (l.val, l))
        
#         # Create a dummy head for the merged linked list
#         dummy = ListNode(0)
#         current = dummy
        
#         while min_heap:
#             # Get the smallest item from the heap
#             val, node = heapq.heappop(min_heap)
#             current.next = ListNode(val)  # Add the smallest node to the merged list
#             current = current.next
            
#             # If there is a next node in the extracted list, push it to the heap
#             if node.next:
#                 heapq.heappush(min_heap, (node.next.val, node.next))
        
#         return dummy.next  # Return the merged list, which starts from dummy.next
