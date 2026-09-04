# https://leetcode.com/problems/house-robber

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        # Handle Small Input
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # Maximum money we can rob up to two houses before.
        two_houses_before = 0

        # Maximum money we can rob up to the previous house.
        one_house_before = 0

        # Process Each House
        for money in nums:

            # Option 1:
            # Skip the current house.
            skip = one_house_before

            # Option 2:
            # Rob the current house.
            # If we rob this house, we cannot rob the previous house.
            rob_current = (two_houses_before + money)

            # Choose the better option.
            current_max = max(skip, rob_current)

            # Move the previous values forward.
            two_houses_before = one_house_before
            one_house_before = current_max

        # Return the maximum amount that can be robbed.
        return one_house_before


# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12
    print(solution.rob([1, 2, 3, 1]))      # Output: 4
    print(solution.rob([3, 1, 3, 100]))    # Output: 103

# I use dynamic programming. For each house, I have two choices: either skip the house or rob it. 
# If I skip it, the maximum money is the same as the previous house, `dp[i-1]`. If I rob it, I cannot rob the previous house, so the amount is `dp[i-2] + nums[i]`. 
# Therefore, `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. 
# Since I only need the previous two DP values, I can optimize the space to O(1). The time complexity is O(n) and the space complexity is O(1).
