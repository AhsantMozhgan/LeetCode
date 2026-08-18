# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        new_start = newInterval[0]
        new_end = newInterval[1]

        # We divide the intervals into three categories:
        # 1. Completely before newInterval
        # 2. Overlapping with newInterval
        # 3. Completely after newInterval
        for current_start, current_end in intervals:
            # Case 1: Before
            # If the current interval ends before newInterval starts, there is no overlap.
            if current_end < new_start:

                # This interval is completely before newInterval. It can be added immediately.
                result.append([current_start, current_end])

            # Case 2: After
            # If the current interval starts after newInterval ends, there is no overlap.
            elif current_start > new_end:

                # Before adding the current interval, we must first add newInterval.
                result.append([new_start, new_end])

                # Add the current interval.
                result.append([current_start, current_end])

                # From this point onward, newInterval has already been inserted.
                # We can add all remaining intervals without changing them.
                result.extend(
                    intervals[intervals.index([current_start, current_end]) + 1:]
                )

                return result


            # Case 3: Overlap
            # Otherwise, the current interval overlaps with newInterval.
            else:

                # Expand newInterval so that it covers both intervals. Keep the smallest start.
                new_start = min(new_start, current_start)

                # Keep the largest end.
                new_end = max(new_end, current_end)

        # Add New Interval
        # If we reach the end of the loop, newInterval has not been added yet. Add the merged interval now.
        result.append([new_start, new_end])

        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.insert([[1, 3], [6, 9]], [2, 5]))          # Output: [[1, 5], [6, 9]]
    print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # Output: [[1, 2], [3, 10], [12, 16]]
    print(solution.insert([], [5, 7]))                        # Output: [[5, 7]]
    print(solution.insert([[1, 5]], [2, 3]))                  # Output: [[1, 5]]

# The intervals are already sorted by their start times, so I don't need to sort them. I divide the problem into three parts. 
# First, I add all intervals that end before the new interval starts. Then I merge every overlapping interval by taking the minimum start and maximum end. 
# Finally, I add the merged interval and append all remaining intervals, which are completely after it.

# ---

# The existing intervals are already sorted and non-overlapping, so I don’t need to insert the new interval and re-sort everything. I can handle them in three simple stages.

# First, I copy every interval that ends before the new interval starts. Those cannot possibly overlap, so they go straight into the result.

# Second, I process the overlapping region. Two intervals overlap when the current one starts at or before the new interval ends. For each of those I expand the new interval by taking the smaller start and the larger end.

# Third, once I reach an interval that starts after the merged new interval has ended, I know that this interval and everything after it belong after the new one. So I append the fully merged new interval once, then copy the remaining intervals unchanged.

# This works cleanly because the input is sorted: all non-overlapping intervals that come before appear first, the overlapping ones form a contiguous block, and everything else comes afterward.

# ---


# OR
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         merged = []
#         i = 0
#         n = len(intervals)

#         # Add all intervals ending before newInterval starts
#         while i < n and intervals[i][1] < newInterval[0]:
#             merged.append(intervals[i])
#             i += 1

#         # Merge overlapping intervals
#         while i < n and intervals[i][0] <= newInterval[1]:
#             newInterval[0] = min(newInterval[0], intervals[i][0])
#             newInterval[1] = max(newInterval[1], intervals[i][1])
#             i += 1
        
#         # Add the merged newInterval
#         merged.append(newInterval)

#         # Add remaining intervals
#         while i < n:
#             merged.append(intervals[i])
#             i += 1

#         return merged
