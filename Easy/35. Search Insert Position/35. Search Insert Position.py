# https://leetcode.com/problems/search-insert-position

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Initialize Search Range
        # left and right represent the current search range.
        left = 0
        right = len(nums) - 1

        # Binary Search
        while left <= right:

            # Find the middle index.
            middle = (left + right) // 2

            # Target Found
            if nums[middle] == target:
                return middle

            # Target Is Larger
            # If target is greater than the middle value, search the right half.
            elif target > nums[middle]:
                left = middle + 1

            # Target Is Smaller
            # If target is smaller than the middle value, search the left half.
            else:
                right = middle - 1

        # Target Not Found
        # When the loop ends, left is exactly the position where target should be inserted.
        return left


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.searchInsert([1, 3, 5, 6], 5))  # Output: 2
    print(solution.searchInsert([1, 3, 5, 6], 2))  # Output: 1
    print(solution.searchInsert([1, 3, 5, 6], 7))  # Output: 4
    print(solution.searchInsert([1, 3, 5, 6], 0))  # Output: 0


# The array is sorted, so I use binary search instead of checking every element. I maintain a search range using `left` and `right`. 
# At each step, I compare the middle value with the target. If the target is larger, I search the right half. If it is smaller, I search the left half. 
# If the target is not found, the loop ends when `left` passes `right`, and `left` represents the position where the target should be inserted. 
# The time complexity is O(log n) and the space complexity is O(1).
