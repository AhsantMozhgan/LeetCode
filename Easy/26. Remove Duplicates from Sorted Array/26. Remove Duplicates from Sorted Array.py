# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # A sorted array with 0 or 1 element already has no duplicates.
        if len(nums) <= 1:
            return len(nums)

        # The first element is always unique.
        write_index = 1

        # Read each remaining element.
        for read_index in range(1, len(nums)):

            # If the current number is different from the last unique number,
            # keep it by writing it at the next available position.
            if nums[read_index] != nums[write_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        # write_index is the number of unique elements.
        return write_index
        

# Since the array is sorted, all duplicates sit next to each other.  

# I use a two-pointer approach. `write_index` marks the position where the next unique element should go.
# I start it at 1 because the first element is always unique.  

# I walk through the array with `read_index`. Whenever I see an element that is different from 
# the last unique one (the one at `write_index - 1`), I copy it to `write_index` and move `write_index` forward.  

# At the end, `write_index` is the count of unique elements, 
# and the first `write_index` positions of the array contain those unique values.  

# It runs in O(n) time and uses only O(1) extra space.
