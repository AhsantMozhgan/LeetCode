# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:

        # Base Cases
        # There is one way to reach the first step.
        if n <= 2:
            return n

        # Number of ways to reach the previous two steps.
        one_step_before = 2
        two_steps_before = 1

        # Build The Solution
        # Calculate the number of ways to reach each step from 3 to n.
        for step in range(3, n + 1):

            # We can reach this step from:
            # 1. The previous step
            # 2. Two steps before
            current_ways = (one_step_before + two_steps_before)

            # Move the previous values forward.
            two_steps_before = one_step_before
            one_step_before = current_ways

        # Return the number of ways to reach the nth step.
        return one_step_before

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(2))  # Output: 2
    print(solution.climbStairs(3))  # Output: 3
    print(solution.climbStairs(5))  # Output: 8

# I use dynamic programming. To reach step `n`, the last move must come either from step `n-1` or from step `n-2`, because we can climb either one or two steps at a time. 
# Therefore, `ways[n] = ways[n-1] + ways[n-2]`. The base cases are `ways[1] = 1` and `ways[2] = 2`. 
# Since I only need the previous two values to calculate the current value, I can optimize the space from O(n) to O(1). 
# The time complexity is O(n) and the space complexity is O(1).

# ---
# OR

# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         # Base cases for n = 1 and n = 2
#         if n <= 2:
#             return n

#         # Create an array to store the number of ways to reach each step
#         dp = [0] * (n + 1)

#         # Base case initializations
#         dp[1] = 1  # There is 1 way to get to the first step
#         dp[2] = 2  # There are 2 ways to get to the second step

#         # Fill the dp array for steps from 3 to n
#         for current_step in range(3, n + 1):
#             dp[current_step] = dp[current_step - 1] + dp[current_step - 2]
            

#         # Return the number of ways to reach the nth step
#         return dp[n]


# # How I’d say it verbally in an interview:

# # This is a dynamic programming problem.  

# # The key insight is that to reach step n you can only come from step n-1 (by taking one step) or from step n-2 (by taking two steps). 
# #So the number of ways to reach n is just the sum of the ways to reach n-1 and n-2.  

# # I keep an array where `ways[current_step]` stores the number of ways to reach step current_step.
# # I set the base cases for steps 1 and 2, then fill the rest of the array from 3 up to n using that recurrence.  

# # At the end I return `ways[n]`.  

# # It runs in O(n) time and uses O(n) space.
