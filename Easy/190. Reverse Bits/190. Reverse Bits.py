# https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:

        # Result
        # This will store the reversed 32-bit number.
        result = 0

        # Process 32 Bits
        # We must process exactly 32 bits.
        # Even if the number has leading zeros, those zeros are still part of the 32-bit representation.
        for _ in range(32):

            # Get Last Bit
            # n & 1 extracts the rightmost bit of n.
            # Example:
            # n = 1011
            # ----
            # 0001
            # So:
            # n & 1 = 1
            bit = n & 1

            # Shift Result Left
            # Move the current result one position to the left.
            # This creates an empty position for the new bit.
            result = result << 1

            # Add Current Bit
            # Add the extracted bit to the rightmost position.
            result = result | bit

            # Shift n Right
            # Remove the rightmost bit that we just processed.
            n = n >> 1

        # Return Result
        # All 32 bits have now been reversed.
        return result



# Example Usage
if __name__ == "__main__":
    solution = Solution()
    n = 43261596  # Example input (in decimal)
    result = solution.reverseBits(n)
    print(result)  # Expected output: 964176192 (which is 00000010100101000001111010011100 in binary)


    
# I need to reverse exactly 32 bits. I process the bits from right to left. For each iteration, I extract the least significant bit using `n & 1`. 
# Then I place that bit in its reversed position using `bit << (31 - i)`. Finally, I shift `n` to the right to process the next bit. 
# After 32 iterations, the result contains the reversed 32-bit integer.


# ---

# OR
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         result = 0
        
#         for _ in range(32):
#             # Extract the least significant bit (LSB)
#             result <<= 1  # Shift result to the left
#             result |= (n & 1)  # Add the LSB of n to result
#             n >>= 1  # Shift n to the right
        
#         return result
