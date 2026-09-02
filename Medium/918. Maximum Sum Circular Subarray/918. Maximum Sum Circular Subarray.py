# https://leetcode.com/problems/maximum-sum-circular-subarray

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # Initialize Values
        # Maximum subarray sum without wrapping around.
        current_max = nums[0]
        best_max = nums[0]

        # Minimum subarray sum.
        # We will use this to find the maximum sum that wraps around.
        current_min = nums[0]
        best_min = nums[0]

        # Total sum of the array.
        total_sum = nums[0]

        # Process The Array
        for num in nums[1:]:

            # Maximum Subarray
            current_max = max(num, current_max + num)
            best_max = max(best_max, current_max)

            # Minimum Subarray
            # Find the smallest contiguous subarray.
            current_min = min(num, current_min + num)
            best_min = min(best_min, current_min)

            # Add current number to the total array sum.
            total_sum += num

        # Handle All-Negative Case
        # If best_max is negative, every number is negative.
        # In that case, using:
        # total_sum - best_min
        # would incorrectly represent an empty subarray.
        if best_max < 0:
            return best_max

        # Calculate Circular Maximum
        # Remove the minimum subarray from the total array.
        circular_sum = total_sum - best_min

        # Return Best Answer
        # The answer is either:
        # 1. A normal maximum subarray
        # 2. A circular maximum subarray
        return max(best_max, circular_sum)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    A = [1, -2, 3, -2]
    print(solution.maxSubarraySumCircular(A))  # Output: 3

    A = [5, -3, 5]
    print(solution.maxSubarraySumCircular(A))  # Output: 10

    A = [-3, -2, -3]
    print(solution.maxSubarraySumCircular(A))  # Output: -2



# I split the problem into two cases. The maximum subarray either does not wrap around, which I solve using Kadane's Algorithm, or it wraps around the end of the array. 
# For the circular case, I find the minimum subarray and subtract it from the total sum, because removing the minimum middle section leaves the maximum circular subarray. 
# So the circular result is `total_sum - minimum_subarray`. There is one important edge case: 
# if all numbers are negative, the circular formula would produce zero by effectively choosing an empty subarray, so in that case I return the normal maximum subarray. 
# The time complexity is O(n) and the space complexity is O(1).

# ---
# # OR

# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         def kadane(arr):
#             max_sum = current_sum = arr[0]
#             for num in arr[1:]:
#                 current_sum = max(num, current_sum + num)
#                 max_sum = max(max_sum, current_sum)
#             return max_sum
        
#         # Case 1: Non-circular
#         non_circular_max = kadane(nums)
        
#         # Case 2: Circular
#         total_sum = sum(nums)
#         # Inverting the values to find the minimum subarray sum
#         for i in range(len(nums)):
#             nums[i] = -nums[i]
        
#         min_subarray_sum = kadane(nums)
#         circular_max = total_sum + min_subarray_sum # Because we inverted the signs
        
#         # If all numbers are negative, return non_circular_max
#         if non_circular_max < 0:
#             return non_circular_max
        
#         return max(non_circular_max, circular_max)