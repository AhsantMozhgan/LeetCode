# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        current_sum = 0
        min_length = float("inf")       # OR min_length = len(nums) + 1

        for right in range(len(nums)):

            # Add the current number to the window.
            current_sum += nums[right]

            # Shrink the window while its sum is large enough.
            while current_sum >= target:

                # Update the minimum length.
                min_length = min(
                    min_length,
                    right - left + 1
                )

                # Remove the leftmost number.
                current_sum -= nums[left]
                left += 1

        # Return 0 if no valid subarray was found.
        if min_length == float("inf"):
            return 0

        return min_length


# I use a sliding window with two pointers. 
# I expand the window by moving the right pointer and adding each number to the current sum.
#  Once the sum reaches the target, I update the minimum length and shrink the window from 
#  the left while the sum is still at least the target. Because all numbers are positive, 
#  expanding increases the sum and shrinking decreases it.