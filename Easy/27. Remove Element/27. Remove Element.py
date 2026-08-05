# https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        write_index = 0

        # Read every element once.
        for read_index in range(len(nums)):

            # Keep only the elements that are not equal to val.
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1

        # write_index is the number of remaining elements.
        return write_index



# I’d use a two-pointer approach.  

# I keep a `write_index` that tracks where the next element I want to keep should go.  

# I walk through the array with a `read_index`. Whenever I find an element that is not equal to `val`, I copy it to the `write_index` position and then move `write_index` forward.  

# At the end, `write_index` is exactly the new length of the array after all occurrences of `val` have been removed.  

# It runs in O(n) time and uses only O(1) extra space.