# https://leetcode.com/problems/combinations

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # Store all valid combinations.
        result = []

        # Backtracking
        # start:
        # The number where we should start choosing from.
        # current:
        # The combination built so far.
        def backtrack(start, current):

            # Base Case
            # If we have selected k numbers, we have a complete combination.
            if len(current) == k:
                result.append(current.copy())
                return

            # Try Every Number
            for number in range(start, n + 1):

                # Choose the current number.
                current.append(number)

                # Continue choosing numbers after the current number.
                backtrack(number + 1, current)

                # Backtrack:
                # Remove the number we just chose.
                current.pop()

        # Start choosing from number 1 with an empty combination.
        backtrack(1, [])

        # Return all combinations.
        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    n = 4  # Total elements
    k = 2  # Elements to choose
    result = solution.combine(n, k)
    print(result)  # Expected output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


# I use backtracking to generate all combinations of k numbers from 1 to n. I keep a current combination and a start value that tells me which numbers are still available. 
# For each number from start to n, I choose it, recursively continue with number + 1, and then remove it when I backtrack. 
# Using number + 1 ensures that numbers are selected in increasing order, so we never generate duplicate combinations such as [2,1] when [1,2] already exists.

# ---
# # OR
# class Solution:
#     def combine(self, n: int, k: int):
#         results = []
#         combination = []

#         def backtrack(start: int):
#             if len(combination) == k:
#                 results.append(list(combination))  # Found a valid combination
#                 return
#             for i in range(start, n + 1):
#                 combination.append(i)  # Choose the current element
#                 backtrack(i + 1)  # Move on to the next element
#                 combination.pop()  # Backtrack

#         backtrack(1)  # Start with the first element
#         return results