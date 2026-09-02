# https://leetcode.com/problems/combination-sum

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # Store all valid combinations.
        result = []

        # Backtracking
        # start:
        # The index where we can start choosing candidates.
        # current:
        # The combination built so far.
        # remaining:
        # How much more we need to reach the target.
        def backtrack(start, current, remaining):

            # Target Reached
            # If remaining becomes 0, we found a valid combination.
            if remaining == 0:
                result.append(current.copy())
                return

            # Target Exceeded
            # If remaining becomes negative, the current combination is too large.
            if remaining < 0:
                return

            # Try Candidates
            for i in range(start, len(candidates)):

                # Choose the candidate.
                current.append(candidates[i])

                # We use i instead of i + 1 because the same number can be used multiple times.
                backtrack(i, current, remaining - candidates[i])

                # Backtrack
                # Remove the candidate so we can try another choice.
                current.pop()

        # Start from index 0 with the full target.
        backtrack(0, [], target)

        # Return all valid combinations.
        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    candidates = [2, 3, 6, 7]  # List of candidates
    target = 7  # Target sum
    result = solution.combinationSum(candidates, target)
    print(result)  # Expected output: [[2, 2, 3], [7]]

# I use backtracking to generate combinations whose sum equals the target. I keep a start index to avoid generating duplicate combinations in different orders. 
# For each candidate, I add it to the current combination and recursively reduce the remaining target. I pass the same index `i` instead of `i + 1` because each candidate can be used unlimited times. 
# When the remaining target becomes zero, I save the combination. If it becomes negative, I stop exploring that branch.


# # OR
# class Solution:
#     def combinationSum(self, candidates, target):
#         results = []

#         def backtrack(start, current_combination, current_sum):
#             if current_sum == target:
#                 results.append(list(current_combination))  # Found a valid combination
#                 return
#             if current_sum > target:
#                 return  # Exceeded the target, no need to continue

#             for i in range(start, len(candidates)):
#                 # Choose the current candidate
#                 current_combination.append(candidates[i])
#                 # Since the same number can be chosen multiple times, we pass `i` instead of `i + 1`
#                 backtrack(i, current_combination, current_sum + candidates[i])
#                 current_combination.pop()  # Backtrack to explore the next candidate

#         backtrack(0, [], 0)  # Start backtracking from the first index
#         return results

