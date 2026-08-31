# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:
            
            # Remove the rightmost 1 bit
            n = n & (n - 1)

            count += 1

        return count

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    n = 11  # Binary representation: 00000000000000000000000000001011
    result = solution.hammingWeight(n)
    print(result)  # Expected output: 3

# I use Brian Kernighan's algorithm to count the set bits. The key observation is that `n & (n - 1)` removes the rightmost set bit from `n`. 
# So I repeatedly apply this operation and increment a counter. When `n` becomes zero, the counter contains the number of 1 bits. 
# Why does `n & (n - 1)` remove one `1`? Subtracting one flips the rightmost `1` to `0` and changes all bits after it to `1`. ANDing the original number with `n - 1` therefore clears that rightmost `1`.

# ---
# # OR
# # Method 1: Iterative Bit Manipulation
# class Solution:
#     def hammingWeight(self, n: int) -> int:

#         # Count
#         # This variable keeps track of how many 1 bits we have found.
#         count = 0

#         # Process The Bits
#         # Continue while n still contains bits.
#         while n > 0:

#             # Get Last Bit
#             # n & 1 checks the rightmost bit.
#             # Example:
#             # n = 1011
#             #
#             #       1011
#             #   &   0001
#             #   ----------
#             #       0001
#             #
#             # So:
#             #
#             # n & 1 = 1
#             #
#             bit = n & 1

#             # Check If Bit Is 1
#             # If the last bit is 1, increase the count.
#             if bit == 1:
#                 count += 1

#             # Move To Next Bit
#             # Shift n one position to the right.
#             # This removes the bit we just processed.
#             n >>= 1

#         # Return Count
#         # Return the total number of 1 bits.
#         return count
