# https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # Create Two Dummy Nodes
        # One list will contain nodes with values smaller than x.
        # The other list will contain nodes with values greater than or equal to x.
        # Example:
        # x = 3
        # less:
        # dummy → ...
        #
        # greater_or_equal:
        # dummy → ...
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        # Create Two Pointers
        # less_tail points to the end of the smaller-values list.
        less_tail = less_dummy

        # greater_tail points to the end of the greater/equal list.
        greater_tail = greater_dummy

        # Traverse the List
        # Process every node in the original linked list.
        current = head

        while current:
            # Save the next node before changing current.next.
            next_node = current.next

            # Value < x
            # If the current value is smaller than x, add it to the first list.
            if current.val < x:
                less_tail.next = current
                less_tail = current

            # Value >= x
            # Otherwise, add it to the second list.
            else:
                greater_tail.next = current
                greater_tail = current

            # Move to the next node in the original list.
            current = next_node

        # End the Second List
        # The second list must end with None.
        greater_tail.next = None

        # Connect Two Lists
        # Connect the end of the smaller list to the beginning of the greater/equal list.
        less_tail.next = greater_dummy.next

        # Return Result
        # less_dummy.next is the head of the final linked list.
        return less_dummy.next

# Example usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    solution = Solution()
    x = 3
    new_head = solution.partition(head, x)

    # Print the new linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# I use two linked lists. The first contains nodes with values less than `x`, and the second contains nodes with values greater than or equal to `x`. I use dummy nodes to simplify handling the heads of both lists. I traverse the original list once and append each node to the appropriate list, which also preserves the original relative order. Finally, I terminate the second list with `None`, connect the end of the first list to the second list, and return the head of the first list. The time complexity is O(n) because I visit every node once, and the extra space complexity is O(1) because I reuse the existing nodes and only create two dummy nodes.

# ---

# I need to rearrange the list so that every node with a value less than x comes before every node with a value greater than or equal to x, while keeping the relative order inside each group.

# I create two dummy nodes to build two separate lists: one for values less than x and one for values greater than or equal to x. Each list also has a tail pointer so I can append in constant time.

# I walk through the original list once. Before I change any next pointer, I save the next original node. Then I attach the current node to the appropriate list and advance that list’s tail.

# After the traversal I set the greater-list’s tail.next to None. This is important — otherwise a leftover link from the original list can create a cycle or an incorrect structure.

# Finally I connect the end of the less-than list to the head of the greater-or-equal list and return the node after the less-than dummy. Because I always append in the order I encounter the nodes, the relative order inside both partitions is preserved.

# The whole thing is a single pass, so O(n) time and O(1) extra space.
