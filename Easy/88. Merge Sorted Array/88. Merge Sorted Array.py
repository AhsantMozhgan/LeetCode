# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        last_num1_index = m - 1  # Last index of the valid elements in nums1
        last_num2_index = n - 1  # Last index of nums2
        write_index = m + n - 1  # Last index of nums1 (considering total size)

        # Compare the largest remaining values in both arrays
        while last_num1_index >= 0 and last_num2_index >= 0:
            if nums1[last_num1_index] > nums2[last_num2_index]:
                nums1[write_index] = nums1[last_num1_index]
                last_num1_index -= 1
            else:
                nums1[write_index] = nums2[last_num2_index]
                last_num2_index -= 1

            write_index -= 1

        # Copy any remaining elements from nums2 (if any)
        while last_num2_index >= 0:
            nums1[write_index] = nums2[last_num2_index]
            last_num2_index -= 1
            write_index -= 1


# This merges two sorted arrays into nums1 in-place, using a three-pointer approach that works from the end.

# I keep three indices: one at the end of the actual numbers in nums1, one at the end of nums2, and one at the very end of nums1 (which already has enough empty space).

# I compare the largest remaining elements from each array and write the larger one at the current write position, then move that array’s pointer and the write pointer backward.

# Once one of the arrays is exhausted, if any elements are left in nums2 I just copy them into nums1. I don’t need to touch the remaining nums1 elements because they’re already in the right place.

# It runs in O(m + n) time and uses only O(1) extra space.
