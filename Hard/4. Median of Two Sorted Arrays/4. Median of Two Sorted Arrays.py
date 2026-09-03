# https://leetcode.com/problems/median-of-two-sorted-arrays

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always Binary Search On Smaller Array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Length of each array.
        m = len(nums1)
        n = len(nums2)

        # Initialize Search Range
        left = 0
        right = m

        # Total number of elements that should be on the left side.
        half = (m + n + 1) // 2

        # Binary Search
        while left <= right:

            # Partition position in nums1.
            partition1 = (left + right) // 2

            # Remaining elements needed on the left side come from nums2.
            partition2 = half - partition1

            # Boundary Values
            left_max_1 = (nums1[partition1 - 1] if partition1 > 0 else float("-inf"))

            right_min_1 = (nums1[partition1] if partition1 < m else float("inf"))

            left_max_2 = (nums2[partition2 - 1] if partition2 > 0 else float("-inf"))

            right_min_2 = (nums2[partition2] if partition2 < n else float("inf"))


            # Correct Partition
            if (left_max_1 <= right_min_2 and left_max_2 <= right_min_1):

                # Odd Number Of Elements
                if (m + n) % 2 == 1:
                    return max(left_max_1, left_max_2)

                # Even Number Of Elements
                return (max(left_max_1, left_max_2) + min(right_min_1, right_min_2)) / 2


            # Partition1 Is Too Far Right
            elif left_max_1 > right_min_2:
                right = partition1 - 1


            # Partition1 Is Too Far Left
            else:
                left = partition1 + 1

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
    print(solution.findMedianSortedArrays([0, 0], [0, 0]))  # Output: 0.0
    print(solution.findMedianSortedArrays([], [1]))  # Output: 1.0
    print(solution.findMedianSortedArrays([2], []))  # Output: 2.0


# I use binary search on the smaller array to find a correct partition between the two sorted arrays. 
# The goal is to put half of all elements on the left side and the rest on the right side. 
# For every partition, I look at the four boundary values: the maximum values on the left and the minimum values on the right from both arrays. 
# The partition is correct when the left maximum of each array is less than or equal to the right minimum of the other array. 
# If the partition is too far right, I move left. If it is too far left, I move right. 
# Once the partition is correct, the median comes from the maximum of the left side for an odd total length, or the average of the maximum left value and minimum right value for an even total length. 
# The time complexity is O(log(min(m, n))) and the space complexity is O(1).
