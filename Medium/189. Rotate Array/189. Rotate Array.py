# https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        k = k % n  # In case k is greater than n
        
        # Function to reverse a segment of the array
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining n-k elements
        reverse(k, n - 1)



# I’d rotate the array in place using the three-reversal technique.  

# A right rotation by k means the last k elements move to the front while keeping their relative order.  

# First I take k modulo n so that any rotation larger than the array length is handled correctly.  

# Then I reverse the entire array — this brings the last k elements to the front, but they’re now in reverse order.  

# Next I reverse the first k elements to put them back in the correct order, and finally I reverse the remaining n − k elements.  

# Each reversal is done with two pointers that swap from the outside toward the center.  

# The whole process modifies the array in place, runs in O(n) time, and uses only O(1) extra space.



# OR
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         # Time: O(n)
#         # Space: O(n)
#         k = k % len(nums) # In case k is greater than n
        
#         nums[:] = nums[-k:] + nums[:-k]
