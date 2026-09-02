# https://leetcode.com/problems/maximum-subarray

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Initialize Values
        # current_sum:
        # Maximum sum of a subarray ending at the current position.
        current_sum = nums[0]

        # best_sum:
        # Maximum subarray sum found anywhere in the array.
        best_sum = nums[0]

        # Process The Array
        for i in range(1, len(nums)):

            # Decide Whether To Extend Or Start Fresh
            # Option 1:
            # Add nums[i] to the previous subarray.
            extend_sum = current_sum + nums[i]

            # Option 2:
            # Start a new subarray from nums[i].
            start_new_sum = nums[i]

            # Keep the better option.
            current_sum = max(extend_sum, start_new_sum)

            # Update Global Maximum
            # current_sum represents the best subarray ending at this position.
            # Compare it with the best answer found so far.
            best_sum = max(best_sum, current_sum)

        # Return the best subarray sum.
        return best_sum


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print(solution.maxSubArray([1]))                       # Output: 1
    print(solution.maxSubArray([5,4,-1,7,8]))              # Output: 23
    print(solution.maxSubArray([-1,-2,-3]))                # Output: -1



# I use Kadane's Algorithm. For each number, I decide whether to extend the current subarray or start a new subarray from the current number. 
# I store the better choice in `current_sum`. Then I update `best_sum` with the maximum sum seen so far. 
# This works because if the previous subarray has a negative contribution, starting fresh is always better. 
# The time complexity is O(n) and the space complexity is O(1).


# # ---
# # OR
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # Initialize variables
#         current_sum = nums[0]
#         max_sum = nums[0]
        
#         # Iterate through the array starting from the second element
#         for i in range(1, len(nums)):
#             current_sum = max(nums[i], current_sum + nums[i])  # Update current_sum
#             max_sum = max(max_sum, current_sum)  # Update max_sum
        
#         return max_sum