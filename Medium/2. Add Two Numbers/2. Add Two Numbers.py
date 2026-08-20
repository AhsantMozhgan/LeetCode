# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node is a temporary starting point for our result.
        # It makes it easier to build the linked list without handling the first node separately.
        dummy = ListNode(0)

        # current_node points to the last node in our result list.
        current_node = dummy

        # Stores the value that must be carried to the next digit.
        carry = 0

        # Continue while at least one list still has a digit, or there is a carry left.
        while l1 or l2 or carry:

            # Get First Digit
            # If l1 still has a node, use its value. Otherwise use 0.
            value1 = l1.val if l1 else 0

            # Get Second Digit
            # If l2 still has a node, use its value. Otherwise use 0.
            value2 = l2.val if l2 else 0

            # Add the Digits: digit from l1 + digit from l2 + previous carry
            total = value1 + value2 + carry

            # The digit we store in the current node is the remainder after dividing by 10.
            digit = total % 10

            # The value that moves to the next position.
            carry = total // 10

            # Add the calculated digit to our result linked list.
            current_node.next = ListNode(digit)

            # Move current_node to the newly created node.
            current_node = current_node.next

            # Move Input Pointers
            # Move l1 forward if there are more digits.
            if l1:
                l1 = l1.next

            # Move l2 forward if there are more digits.
            if l2:
                l2 = l2.next

        # dummy itself is not part of the answer. The actual result starts at dummy.next.
        return dummy.next


# Example usage
if __name__ == "__main__":
    # Create the first linked list 2 -> 4 -> 3 (342)
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    
    # Create the second linked list 5 -> 6 -> 4 (465)
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print the result
    while result:
        print(result.val, end=' -> ' if result.next else '\n')
        result = result.next  # Move to the next node

# The digits are stored in reverse order, so I can add the numbers from left to right, starting with the least significant digit. 
# I use a carry variable to handle sums greater than 9. For each position, I add the two digits and the carry, store `total % 10` in a new node, 
# and update the carry using `total // 10`. I use a dummy node to simplify building the result linked list.

# ---
# The two linked lists store digits in reverse order, so the head of each list holds the least significant digit. That lets me add the numbers from left to right exactly the way we do addition by hand.

# I start with a dummy node to simplify building the result list. A pointer called `current` always sits on the last node of the result, so I can attach each new digit without treating the first node as a special case.

# On every step I read the digit from the current node of `l1` and of `l2`. If either list has already ended I treat its digit as zero. I add those two digits together with the carry left over from the previous position.

# The digit I store in the result is `total % 10` (the ones place). The carry that goes to the next position is `total // 10` (the tens place).

# I keep going as long as either list still has nodes or a non-zero carry remains. That final carry check is important for cases such as 5 + 5, which must produce the list `[0, 1]`.

# When everything is finished I return `dummy.next`, because the dummy itself is only a placeholder and is not part of the answer.
