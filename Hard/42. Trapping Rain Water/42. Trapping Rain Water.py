# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:

        left_index = 0
        right_index = len(height) - 1

        left_max_height = 0
        right_max_height = 0

        trapped_water = 0

        while left_index < right_index:

            # The left side is the limiting side.
            if height[left_index] < height[right_index]:

                # Update the tallest wall seen from the left.
                left_max_height = max(
                    left_max_height,
                    height[left_index]
                )

                # Water above the current position
                # depends on the tallest wall on the left.
                trapped_water += (
                    left_max_height - height[left_index]
                )

                left_index += 1

            else:

                # Update the tallest wall seen from the right.
                right_max_height = max(
                    right_max_height,
                    height[right_index]
                )

                # Water above the current position
                # depends on the tallest wall on the right.
                trapped_water += (
                    right_max_height - height[right_index]
                )

                right_index -= 1

        return trapped_water


# I use a two-pointer approach. I place one pointer at the left end and one at the right end, and I keep track of the tallest wall seen so far from each side with `left_max_height` and `right_max_height`.

# The amount of water that can be trapped at any position is limited by the shorter of the two boundaries.  
# So whenever the height on the left is smaller (or equal), I process the left side: I update `left_max_height`, add `left_max_height − height[left]` to the answer, and move the left pointer inward.  
# Otherwise I do the symmetric work on the right side.

# The key insight is that when one side is currently shorter, there is already a wall on the opposite side that is at least as tall, so the shorter side alone determines how much water can sit there.

# Each pointer moves inward at most n times, so the whole algorithm runs in O(n) time and uses only O(1) extra space.
