# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Result
        # This will store the unique number.
        result = 0

        # Check Every Bit
        # An integer has 32 bits. We check each bit position from 0 to 31.
        for bit_position in range(32):

            # Count 1 Bits
            # Count how many numbers have a 1 at this position.
            count_ones = 0

            for current_number in nums:

                # Check Current Bit
                # Shift the current number to the right so that the bit we want to check
                # becomes the rightmost bit. Then use & 1 to extract it.
                bit = (current_number >> bit_position) & 1

                # Add the bit to our count.
                count_ones += bit

            # Check Remainder
            # Every duplicate number appears exactly 3 times.
            # Therefore, bits belonging to duplicate numbers appear a multiple of 3 times.
            # If the remainder is 1, this bit belongs to the unique number.
            if count_ones % 3 != 0:

                # Put Bit Into Result
                # Create a 1 at the current bit position.
                result |= (1 << bit_position)


        # Convert To Signed 32-bit
        # If bit 31 is 1, the number represents a negative number in signed 32-bit representation.
        if result >= 2**31:
            result -= 2**32

        # Return Result
        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 2, 3, 2]  # Example input
    result = solution.singleNumber(nums)
    print(result)  # Expected output: 3

# Since every number appears three times except one, I process each bit position independently. 
# For every bit, I count how many numbers have that bit set. The count of bits contributed by the duplicate numbers will always be a multiple of three. 
# So I take the count modulo 3. If the remainder is 1, that bit belongs to the unique number, and I set that bit in the result.

# Why can't you use XOR? XOR works when duplicates appear twice because `a ^ a = 0`. But here numbers appear three times, and `a ^ a ^ a = a`, so XOR cannot cancel the duplicates.


# ---
# # OR
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ones, twos = 0, 0
        
#         for num in nums:
#             # Update twos with the bits that are in ones
#             twos |= ones & num
#             # Update ones with the current number
#             ones ^= num
#             # Identify the bits that appear three times
#             threes = ones & twos
#             # Remove bits in threes from ones and twos
#             ones &= ~threes
#             twos &= ~threes
        
#         return ones

