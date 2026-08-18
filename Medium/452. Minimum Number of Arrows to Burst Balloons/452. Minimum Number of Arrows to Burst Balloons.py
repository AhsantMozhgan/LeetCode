# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # If there are no balloons, we do not need any arrows.
        if not points:
            return 0

        # Sort balloons by their ending position.
        points.sort(key=lambda balloon: balloon[1])

        # We need at least one arrow because there is at least one balloon.
        arrow_count = 1


        # Place the first arrow at the end of the first balloon.
        arrow_position = points[0][1]

        # Process Remaining Balloons
        for start, end in points[1:]:

            # If the current balloon starts at or before the arrow position, the arrow can burst it.
            if start <= arrow_position:
                continue

            # If start > arrow_position the current balloon starts after our previous arrow.
            # We need a new arrow.
            arrow_count += 1

            # Place the new arrow at the end of the current balloon.
            arrow_position = end

        return arrow_count

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # Output: 2
    print(solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))    # Output: 4
    print(solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))    # Output: 2
    print(solution.findMinArrowShots([]))                                  # Output: 0

    
# I sort the balloons by their ending position. Then I place the first arrow at the end of the first balloon. For each following balloon, 
# if its start is less than or equal to the current arrow position, that arrow can burst it, so I continue. Otherwise, the balloon starts after the current arrow, 
# so I need another arrow and place it at the end of that balloon. 
# This greedy strategy minimizes the number of arrows because I always place each arrow as far left as possible while still bursting the earliest-ending balloon.


# ---

# Each balloon is an interval from its start to its end position. An arrow fired at any point x bursts every balloon whose interval contains x.

# To minimize the number of arrows I first sort the balloons by their ending position.  

# I place the first arrow at the end of the balloon that finishes earliest. That choice is greedy but optimal: it guarantees that balloon is burst while keeping the arrow as far to the right as possible, which maximizes the chance of also hitting later overlapping balloons.

# Then I scan the rest of the balloons.  
# - If a balloon starts at or before the current arrow position, the arrow already lies inside it, so it is burst for free and I do nothing.  
# - If a balloon starts after the current arrow, the previous arrow cannot reach it. I therefore increment the arrow count and place a new arrow at the end of this balloon.

# After a single pass the arrow count is the minimum number needed to burst every balloon.
