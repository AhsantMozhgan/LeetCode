# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Result
        # Start with 0 because: 0 ^ number = number
        result = 0

        # Process Every Number
        # XOR every number with result.
        for current_number in nums:

            # XOR
            # If a number appears twice, the two copies cancel each other out:
            # number ^ number = 0
            # The number that appears only once will remain.
            result ^= current_number

        # Return Single Number
        # All duplicate numbers have canceled each other out. Only the unique number remains.
        return result

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 2, 1]  # Example input
    result = solution.singleNumber(nums)
    print(result)  # Expected output: 1


# I use XOR because every number appears twice except one. XOR has the property that a number XORed with itself becomes zero, and XORing with zero returns the original number. 
# So if I XOR every number together, all the duplicate numbers cancel each other out, leaving only the number that appears once.

# Why does XOR work here? Because `a ^ a = 0` and `a ^ 0 = a`. Since every duplicate appears exactly twice, the duplicates cancel out and only the unique number remains.

# Why not use a HashSet?
# A HashSet would work, but it would require O(n) extra space. XOR lets me solve it using O(1) extra space.

# # ---
# # OR Alternative Method: Using a Hash Map
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         counts = {}
#         for num in nums:
#             counts[num] = counts.get(num, 0) + 1  # Count occurrences
            
#         for num, count in counts.items():
#             if count == 1:
#                 return num
