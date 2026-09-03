# https://leetcode.com/problems/ipo

from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # Store Projects
        # Each project is stored as: (required capital, profit)
        projects = sorted(zip(capital, profits))

        # Max heap of available profits.
        # Python has a Min Heap, so we store negative profits to simulate a Max Heap.
        max_heap = []

        # Pointer to the next project in the sorted list.
        project_index = 0

        # Choose At Most K Projects
        for _ in range(k):

            # Add Available Projects
            # Add every project that we can currently afford.
            while (project_index < len(projects) and projects[project_index][0] <= w):

                required_capital, profit = (projects[project_index])

                # Push negative profit because heapq is a Min Heap.
                heapq.heappush(max_heap, -profit)
                project_index += 1

            # No Available Project
            if not max_heap:
                break

            # Choose Maximum Profit
            # Remove the largest profit
            w += -heapq.heappop(max_heap)

        # Return the maximum capital.
        return w



# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 2]))  # Output: 6
    print(solution.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))  # Output: 6


# I use a greedy approach with sorting and a max heap. First, I sort all projects by their required capital. 
# Then, for each of the at most k projects we can select, I add every project whose required capital is less than or equal to our current capital into a max heap. 
# The heap stores the profits of all currently affordable projects, so I can always choose the project with the maximum profit. 
# After completing that project, I add its profit to our capital, which may make additional projects affordable. 
# I repeat this process up to k times. The time complexity is O(n log n + k log n), and the space complexity is O(n).


# # ---
# # OR
# import heapq

# class Solution:
#     def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
#         # Pair up capital and profits, then sort by capital
#         projects = sorted(zip(Capital, Profits))

#         max_profit_heap = []
#         current_project_index = 0
#         n = len(projects)

#         for _ in range(k):
#             # Add all projects that can be afforded with current capital W
#             while current_project_index < n and projects[current_project_index][0] <= W:
#                 # Push the profit of the project into the max-heap
#                 heapq.heappush(max_profit_heap, -projects[current_project_index][1])  # use negative for max-heap
#                 current_project_index += 1

#             # If we can complete any project
#             if max_profit_heap:
#                 # Get the project with the maximum profit
#                 max_profit = -heapq.heappop(max_profit_heap)  # Pop the maximum profit
#                 W += max_profit  # Increase capital by the profit of the selected project

#         return W

