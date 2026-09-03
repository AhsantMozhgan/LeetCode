# https://leetcode.com/problems/find-peak-element

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Initialize Search Range
        left = 0
        right = len(nums) - 1

        # Binary Search
        while left < right:

            # Find the middle index.
            middle = (left + right) // 2

            # Compare Middle With Right
            # If nums[middle] is smaller than nums[middle + 1], we are moving uphill.
            if nums[middle] < nums[middle + 1]:

                # A peak must exist on the right side.
                left = middle + 1

            # Moving Downhill
            else:

                # A peak exists at middle or somewhere on the left.
                right = middle

        # Return Peak
        # left == right, so only one possible position remains.
        return left


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.findPeakElement([1, 2, 3, 1]))  # Output: 2 (index of 3)
    print(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 1 or 5 (indices of 2 or 6)


# I use binary search based on the slope between `middle` and `middle + 1`. 
# If `nums[middle] < nums[middle + 1]`, we are moving uphill, so there must be a peak somewhere on the right, and I move `left` to `middle + 1`. 
# Otherwise, we are moving downhill, so a peak exists at `middle` or somewhere on the left, so I move `right` to `middle`. 
# I continue until `left == right`, and that remaining index is a peak. The time complexity is O(log n) and the space complexity is O(1).
