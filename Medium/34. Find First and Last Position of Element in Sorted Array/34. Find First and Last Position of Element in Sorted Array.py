# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array


from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        
        # Find First Position
        def find_first():
            left = 0
            right = len(nums) - 1

            first_position = -1


            while left <= right:
                middle = (left + right) // 2

                # Target Found
                if nums[middle] == target:

                    # Store this position as a possible first position.
                    first_position = middle

                    # Continue searching on the left side.
                    right = middle - 1


                elif nums[middle] < target:

                    # Target must be on the right.
                    left = middle + 1

                else:

                    # Target must be on the left.
                    right = middle - 1

            return first_position

        # Find Last Position
        def find_last():
            left = 0
            right = len(nums) - 1

            last_position = -1

            while left <= right:

                middle = (left + right) // 2

                # Target Found
                if nums[middle] == target:

                    # Store this position as a possible last position.
                    last_position = middle

                    # Continue searching on the right side.
                    left = middle + 1

                elif nums[middle] < target:

                    # Target must be on the right.
                    left = middle + 1

                else:

                    # Target must be on the left.
                    right = middle - 1

            return last_position

        # Perform Both Searches
        first = find_first()
        last = find_last()

        # Return both positions.
        return [first, last]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))   # Output: [3, 4]
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))   # Output: [-1, -1]
    print(solution.searchRange([], 0))                     # Output: [-1, -1]

# Because the array is sorted, I can use binary search. I perform two binary searches. The first search finds the leftmost occurrence of the target. When I find the target, I store its index and continue searching to the left. The second search finds the rightmost occurrence. When I find the target, I store its index and continue searching to the right. If the target doesn't exist, the stored position remains -1. The time complexity is O(log n) and the space complexity is O(1).


# ---
# OR

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]: 
#         result = [-1, -1]
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right and (result[0] == -1 or result[1] == -1):

#             if result[0] == -1 and nums[left] == target:
#                 result[0] = left
#             if result[1] == -1 and nums[right] == target:
#                 result[1] = right

#             mid = (left + right) // 2

#             if nums[mid] < target:
#                 left = mid + 1
#             elif target < nums[mid]:
#                 right = mid - 1
#             else:
#                 if nums[left] < target:
#                     left += 1
#                 if target < nums[right]:
#                     right -= 1

#         return result
