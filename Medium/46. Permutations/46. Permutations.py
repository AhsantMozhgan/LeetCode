# https://leetcode.com/problems/permutations

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Store all permutations.
        result = []

        # Backtracking
        # current:
        # The permutation built so far.
        # used:
        # Keeps track of which numbers have already been used.
        def backtrack(current, used):

            # Base Case
            # If we have used every number, we have a complete permutation.
            if len(current) == len(nums):
                result.append(current.copy())
                return

            # Try Every Number
            for i in range(len(nums)):

                # Skip numbers that have already been used.
                if used[i]:
                    continue

                # Choose this number.
                current.append(nums[i])
                used[i] = True

                # Continue building the permutation.
                backtrack(current, used)

                # Backtrack
                # Undo our choice so another number can be tried.
                current.pop()
                used[i] = False

        # Start with an empty permutation.
        backtrack([], [False] * len(nums))

        # Return all permutations.
        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]  # Input list
    result = solution.permute(nums)
    print(result)  # Expected output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# I use backtracking to generate all permutations. I keep a current permutation and a boolean array called `used` to track which numbers have already been selected. 
# At each step, I try every unused number, add it to the current permutation, and recursively continue. Once the permutation contains all numbers, I add a copy to the result. 
# After the recursive call, I remove the number and mark it as unused so we can try another choice. Unlike combinations, order matters here, so we don't use a start index.

# # ---
# # OR
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:

#         results = []

#         def backtrack(current_permutation):
#             # If the current permutation is the same length as nums, it's complete
#             if len(current_permutation) == len(nums):
#                 results.append(list(current_permutation))  # Add a copy of the current permutation to results
#                 return
            
#             for num in nums:
#                 if num in current_permutation:
#                     continue  # Skip already used numbers
#                 current_permutation.append(num)  # Choose the current number
#                 backtrack(current_permutation)  # Continue building the permutation
#                 current_permutation.pop()  # Backtrack to explore other possibilities

#         backtrack([])  # Start with an empty permutation
#         return results
