# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:

        # Already at the destination.
        if len(nums) <= 1:
            return 0

        jump_count = 0
        current_jump_end = 0
        farthest_reachable_index = 0
        last_index = len(nums) - 1

        # The last index never needs to make another jump.
        for current_index in range(last_index):

            # Find the farthest position reachable from
            # any index in the current jump range.
            farthest_reachable_index = max(
                farthest_reachable_index,
                current_index + nums[current_index],
            )

            # Once we reach the end of the current jump range,
            # we must make another jump.
            if current_index == current_jump_end:
                jump_count += 1
                current_jump_end = farthest_reachable_index

                # Stop early if the destination is already reachable.
                if current_jump_end >= last_index:
                    break

        return jump_count


# I’d use a greedy approach. Instead of deciding the exact next index to jump to right away, I treat all positions reachable with the current number of jumps as one range.  

# `current_jump_end` marks the end of that current range, and `farthest_reachable_index` tracks the furthest index I can reach from any position inside it.  

# As I walk through the range I continuously update the farthest reachable index.  
# When I actually reach the end of the current range I have to make another jump, so I increment `jump_count` and extend the range to `farthest_reachable_index`.  

# If that new range already reaches or passes the last index, I can stop early.  

# This works because each jump greedily expands my reachable range as far as possible.  
# The algorithm runs in O(n) time and uses only O(1) extra space.
