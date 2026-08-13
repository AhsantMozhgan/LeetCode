# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)  # Update maximum area
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area


# I’d use a two-pointer approach. I start with one pointer at the beginning and one at the end — that gives me the widest possible container.  

# For any pair of lines the area is the distance between the pointers multiplied by the shorter of the two heights, because water would spill over the shorter wall. I compute that area and keep track of the maximum I’ve seen so far.  

# Then I move the pointer that points to the shorter line inward. Moving the taller line can’t help: the width shrinks while the shorter line still limits the height. By moving the shorter line I might find a taller boundary that compensates for the reduced width and produces a larger area.  

# I keep doing this until the two pointers meet. The whole algorithm runs in O(n) time and uses only O(1) extra space.


