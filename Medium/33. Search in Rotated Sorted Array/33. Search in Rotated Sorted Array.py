# https://leetcode.com/problems/search-in-rotated-sorted-array

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initialize Search Range
        left = 0
        right = len(nums) - 1

        # Binary Search
        while left <= right:

            # Find the middle index.
            middle = (left + right) // 2

            # Target Found
            if nums[middle] == target:
                return middle

            # Determine Sorted Half
            # At least one half of the rotated array is sorted.
            if nums[left] <= nums[middle]:

                # The left half is sorted.
                # Check whether target belongs to this range.
                if nums[left] <= target < nums[middle]:

                    # Target is inside the sorted left half.
                    right = middle - 1

                else:
                    # Target is not in the left half.
                    left = middle + 1

            else:

                # The right half is sorted.
                # Check whether target belongs to this range.
                if nums[middle] < target <= nums[right]:

                    # Target is inside the sorted right half.
                    left = middle + 1

                else:
                    
                    # Target is not in the right half.
                    right = middle - 1

        # Target does not exist.
        return -1


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1


# I use binary search, but because the array is rotated, I first determine which half is sorted. 
# At least one half must be sorted. If the left half is sorted, I check whether the target falls within its range. 
# If it does, I search the left half; otherwise, I search the right half. If the right half is sorted, I do the opposite. 
# I continue until I find the target or the search range becomes empty. The time complexity is O(log n) and the space complexity is O(1).



# -----
# OR
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         if len(nums) <= 1 or nums[0] < nums[-1]:
#             return self.searchInsert(nums, target)

#         left, mid, right = 0, 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid - 1] > nums[mid]:
#                 break
#             if nums[mid] > nums[mid + 1]:
#                 mid += 1
#                 break
#             if nums[mid] < nums[left]:
#                 right = mid
#             if nums[mid] > nums[right]:
#                 left = mid

#         second_part = nums[mid] <= target and target <= nums[-1]
#         if second_part:
#             position = self.searchInsert(nums[mid:], target)
#         else:
#             position = self.searchInsert(nums[:mid], target)
#         if position >= 0 and second_part:
#             position += mid
#         return position
        
#     def searchInsert(self, nums: List[int], target: int):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#         return -1
        