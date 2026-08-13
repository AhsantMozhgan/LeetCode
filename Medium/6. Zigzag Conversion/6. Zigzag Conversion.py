# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # If there is only one row, there is no zigzag.
        if numRows == 1 or numRows >= len(s):
            return s

        # Create one string for each row.
        rows = [""] * numRows

        current_row = 0
        moving_down = True

        # Place each character into the correct row.
        for current_character in s:

            rows[current_row] += current_character

            # Change direction when we reach the top or bottom.
            if current_row == numRows - 1:
                moving_down = False

            elif current_row == 0:
                moving_down = True

            # Move to the next row.
            if moving_down:
                current_row += 1
            else:
                current_row -= 1

        # Read all rows from top to bottom.
        return "".join(rows)



# I’d simulate the zigzag pattern row by row instead of building a full 2-D grid.  

# I create one string buffer for each row, then keep track of the current row and the direction I’m moving — down or up.  

# For every character I simply append it to the current row’s buffer.  
# When I hit the bottom row I reverse direction and start going up; when I hit the top row I reverse again and start going down. After each character I move to the next row according to that direction.  

# Once I’ve placed every character, I just concatenate all the row buffers from top to bottom to get the final string.  

# I also handle the edge cases where `numRows` is 1 or greater than or equal to the length of the string — in those cases no rearrangement is needed.  

# The whole solution runs in O(n) time and uses O(n) extra space.