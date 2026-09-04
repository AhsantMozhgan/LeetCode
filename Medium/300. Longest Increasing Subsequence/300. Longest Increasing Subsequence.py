# https://leetcode.com/problems/longest-increasing-subsequence

# Method 1: Dynamic Programming Approach

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Handle Empty Input
        if not nums:
            return 0

        # Create DP Array
        # dp[i] represents the length of the longest increasing subsequence ending at nums[i].
        dp = [1] * len(nums)

        # Compare With Previous
        for i in range(len(nums)):

            for j in range(i):

                # nums[j] can come before nums[i] if nums[j] is smaller.
                if nums[j] < nums[i]:

                    # Add nums[i] to the subsequence ending at j.
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the longest subsequence found anywhere in the array.
        return max(dp)

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    result = solution.lengthOfLIS(nums)
    print(result)  # Expected output: 4 (The LIS is [2, 3, 7, 101])


# I use dynamic programming. I define `dp[i]` as the length of the longest increasing subsequence ending at index `i`. 
# Initially, every `dp[i]` is 1 because every individual number is an increasing subsequence of length one. 
# For each number, I look at all previous numbers. If `nums[j] < nums[i]`, then I can append `nums[i]` to the increasing subsequence ending at `j`, so I update `dp[i]` with `dp[j] + 1`. 
# Finally, I return the maximum value in the DP array because the longest subsequence does not necessarily end at the last element.


# # ---
# # OR
# # Method 2: Binary Search Approach (O(n log n))

# import bisect

# class Solution:
#     def lengthOfLIS(self, nums: list) -> int:
#         if not nums:
#             return 0
        
#         sub = []  # This will store the longest increasing subsequence

#         for num in nums:
#             # Use binary search to find the insertion point for num in sub
#             idx = bisect.bisect_left(sub, num)
#             # If idx is equal to the length of sub, it means num is larger than any element in sub
#             if idx >= len(sub):
#                 sub.append(num)  # Extend the size of the LIS
#             else:
#                 sub[idx] = num  # Replace the existing value with num (maintain the smallest possible end value)

#         return len(sub)  # The length of sub is the length of the LIS
