# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reachable = 0  # Initialize the maximum reachable index
        
        for current_index in range(len(nums)):
            # If the current index is beyond the maximum reachable, we can't proceed.
            if current_index > max_reachable:
                return False
            
            # Update the maximum reachable index
            max_reachable = max(max_reachable, current_index + nums[current_index])

            # If we can reach or surpass the last index, return True
            if max_reachable >= len(nums) - 1:
                return True
        
        # If we finish the loop and haven't reached the last index, return False
        return False


# I’d use a greedy approach and keep track of the farthest index I can currently reach. 
# I start with `max_reachable = 0` because I begin at index 0.  

# As I scan through the array, if the current index is already past `max_reachable`, 
# that position is unreachable, so I return false.  
# Otherwise I update the farthest reachable position to the maximum of what I already 
# have and `current_index + nums[current_index]`.  

# If at any point the reachable range reaches or passes the last index, I can return true early.  
# If I finish the loop without ever reaching the end, I return false.  

# This works because I don’t need to pick a specific jump at each step — I only need to know 
# the farthest position I can get to from any index I’ve already been able to reach.  

# It runs in O(n) time and uses only O(1) extra space.
