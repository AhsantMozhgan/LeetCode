# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Initialize Search Range
        left = 0
        right = len(nums) - 1

        # Binary Search
        while left < right:     # use <, not <=

            # Find the middle index.
            middle = (left + right) // 2

            # Compare Middle With Right
            # If nums[middle] is greater than nums[right], the minimum must be on the right side.
            if nums[middle] > nums[right]:
                left = middle + 1

            # Minimum Is At Middle Or On The Left
            # Otherwise, the minimum is in the left half (including mid).
            else:
                right = middle

        # Return Minimum
        # left == right, so only one possible position remains.
        return nums[left]        # or nums[right] – both are the minimum


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.findMin([3, 4, 5, 1, 2]))  # Output: 1
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
    print(solution.findMin([1]))  # Output: 1


# I use binary search to find the minimum in the rotated sorted array. I compare the middle element with the rightmost element. 
# If `nums[middle]` is greater than `nums[right]`, the rotation point and therefore the minimum must be on the right, so I move `left` to `middle + 1`. 
# Otherwise, the right half is sorted, so the minimum is at `middle` or somewhere on the left, and I move `right` to `middle`. 
# I continue until `left == right`, and that index contains the minimum value. The time complexity is O(log n) and the space complexity is O(1).
