# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            elif current_sum < target:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left
        
        return []  # In case there's no solution (though problem states there's always a valid answer)


# Because the array is already sorted, I can solve this with two pointers. I place one pointer at the start of the array and one at the end.  

# On each step I add the two values they point to.  
# - If the sum equals the target, I return their indices.  
# - If the sum is smaller than the target, I move the left pointer right to increase the sum.  
# - If the sum is larger, I move the right pointer left to decrease it.  

# The sorted order makes these moves safe: advancing the left pointer can only increase the sum, and moving the right pointer left can only decrease it.  

# Since the problem asks for 1-based indices, I return `left + 1` and `right + 1`.  

# The whole solution runs in O(n) time and uses only O(1) extra space.