# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # If there are no intervals, there is nothing to merge.
        if not intervals:
            return []

        # Sort intervals by their starting position.
        intervals.sort(key=lambda interval: interval[0])

        # This list stores the merged intervals.
        result = []

        # Start With First Interval. The first interval can always be added to the result.
        result.append(intervals[0])

        # Process Remaining Intervals. Compare every interval with the last interval in result.
        for current_start, current_end in intervals[1:]:

            # Get the last merged interval.
            last_start, last_end = result[-1]

            # Check For Overlap
            # Two intervals overlap when the current interval starts before or exactly when the previous interval ends.
            if current_start <= last_end:
                # Merge Intervals. Keep the earliest start and the farthest end.
                result[-1][1] = max(
                    last_end,
                    current_end
                )

            # No Overlap. the intervals are separate. They do not overlap.
            else:

                # Add the current interval as a new separate interval.
                result.append(
                    [current_start, current_end]
                )

        # Return all merged intervals.
        return result


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
    print(solution.merge([[1, 4], [4, 5]]))                      # Output: [[1, 5]]
    print(solution.merge([[1, 2], [3, 4], [5, 6]]))              # Output: [[1, 2], [3, 4], [5, 6]]
    print(solution.merge([]))                                     # Output: []

# First, I sort the intervals by their starting position. Then I iterate through them and compare each interval with the last interval in the result. 
# If the current interval starts before or when the previous interval ends, they overlap, so I merge them by keeping the same start and taking the larger end. 
# Otherwise, I add the current interval as a new interval.

# ---
# The brute-force approach would try every pair of numbers, which is O(n²).  

# Instead I use a hash map that stores each number I’ve already seen together with the index where it appeared.  

# As I walk through the list I compute the complement — the value I still need to reach the target — which is simply target minus the current number.  

# I then check whether that complement is already in the map.  
# If it is, I’ve found the two numbers that add up to the target, so I return the stored index of the complement and the current index.  

# If the complement isn’t there yet, I insert the current number and its index into the map so a later number can match against it.  

# I always check before inserting, which automatically prevents using the same element twice.  
# Since the problem guarantees exactly one solution, I will always return from inside the loop.
