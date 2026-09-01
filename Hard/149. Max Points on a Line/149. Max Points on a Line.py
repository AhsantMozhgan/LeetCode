# https://leetcode.com/problems/max-points-on-a-line

from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        # Handle Small Input
        # If there are 0 or 1 points, that number of points is automatically the maximum.
        if len(points) < 2:
            return len(points)

        # Store the maximum number of points found on one line.
        max_points = 0

        # Choose Anchor Point
        # Treat each point as the starting point.
        for i in range(len(points)):

            # Create a HashMap that stores each slope and how many times that slope appears.
            slopes = defaultdict(int)

            # Start with 1 because the anchor point itself counts as a point on the line.
            duplicate_points = 1

            # Compare With Other Points
            # Compare the anchor point with every point after it.
            for j in range(i + 1, len(points)):

                # Calculate dx and dy dx represents the horizontal difference between the points.
                # dy represents the vertical difference between the points.
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                # Handle Duplicate Points
                # If dx and dy are both 0, the two points have exactly the same coordinates.
                if dx == 0 and dy == 0:

                    # Count the duplicate point.
                    duplicate_points += 1

                    # Do not calculate a slope for duplicate points.
                    continue

                # Reduce The Slope
                # Find the greatest common divisor of dx and dy.
                # This allows equivalent slopes to have the same representation.
                divisor = gcd(dy, dx)

                # Divide both values by the GCD to reduce the fraction.
                dy //= divisor
                dx //= divisor

                # Normalize The Sign
                # We want equivalent slopes to always have the same sign.
                if dx < 0:

                    # If dx is negative, make both values positive or move the negative sign to dy.
                    dy = -dy
                    dx = -dx

                # Normalize Vertical Lines
                # For a vertical line, dx is 0.
                elif dx == 0:

                    # All vertical lines use the same representation:
                    # (1, 0)
                    dy = 1

                # Create Slope Key
                # Store the normalized slopeas a tuple.
                slope = (dy, dx)

                # Increase the count for this particular slope.
                slopes[slope] += 1

            # Find Most Common Slope
            # Find the largest number of points sharing the same slope.
            current_max = max(slopes.values(), default=0)

            # Update Maximum
            # current_max counts the other points sharing the same slope.
            # duplicate_points includes the anchor and its duplicates.
            #
            max_points = max(max_points,current_max + duplicate_points)

        # Return Answer
        # Return the largest number of points found on one line.
        return max_points

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    points = [[1,1],[2,2],[3,3]]  # Example input
    result = solution.maxPoints(points)
    print(result)  # Expected output: 3

# For each point, I treat it as an anchor point and calculate the slope between it and every other point. 
# I store each normalized slope in a hash map and count how many points have that slope. 
# I use GCD to reduce the `(dy, dx)` pair so equivalent slopes have the same representation. 
# I also normalize the sign and handle vertical lines separately. Duplicate points are counted separately 
# because they don't have a valid slope. Finally, I add the duplicate count to the most frequent slope count.
