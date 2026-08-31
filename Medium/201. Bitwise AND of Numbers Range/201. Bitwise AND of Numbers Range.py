# https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        while left < right:

            # Remove the rightmost 1 bit from right.
            right &= right - 1

        return right

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    left, right = 5, 7  # Example input
    result = solution.rangeBitwiseAnd(left, right)
    print(result)  # Expected output: 4 (Binary: 100)

# The key observation is that any bit that changes within the range will become zero in the final AND. 
# I repeatedly clear the rightmost set bit of `right` using `right &= right - 1`. This removes the bits that cannot remain set across the entire range. 
# When `right` is no longer greater than `left`, the remaining value is the common bitwise AND of the range.

#  Why `right &= right - 1`? It removes the rightmost set bit of `right`. Every bit we remove is a bit that cannot stay set across the entire range.

# ---
# # OR
# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:

#         # Count Shifts
#         # This keeps track of how many times we shift the numbers to the right.
#         shift_count = 0

#         # Find Common Prefix
#         # We keep shifting both numbers to the right until they become equal.
#         # The part that remains is the common binary prefix.
#         while left != right:

#             # Move left one bit to the right.
#             left >>= 1

#             # Move right one bit to the right.
#             right >>= 1

#             # Remember how many positions we shifted.
#             shift_count += 1

#         # Restore Bit Positions
#         # The common prefix is currently shifted to the right.
#         # Move it back to its original position.
#         return left << shift_count
