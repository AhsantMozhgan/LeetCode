# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:  # If the array has 2 or fewer elements, we return its length.
            return len(nums)

        write_index = 2  # Start writing from the third position

        for read_index in range(2, len(nums)):
            # We check if the current element is different from the element at write_index - 2
            if nums[read_index] != nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index


# Because the array is sorted, duplicates sit next to each other. The goal is to keep each number at most twice.  

# I use a `write_index` that marks where the next valid element should go. I start it at 2, since the first two elements are always allowed.  

# Then I scan from index 2 onward. For each number I compare it with `nums[write_index - 2]`. If they’re different, 
# writing this number won’t create more than two copies, so I place it at `write_index` and move `write_index` forward.  

# At the end, `write_index` is the new length of the array, and the first `write_index` elements are the valid ones.  

# It runs in O(n) time and uses only O(1) extra space.
