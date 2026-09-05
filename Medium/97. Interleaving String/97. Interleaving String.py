# https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        # Use s2 as the shorter string to reduce memory usage.
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for j in range(1, len(s2) + 1):
            dp[j] = (dp[j - 1] and s2[j - 1] == s3[j - 1])


        for i in range(1, len(s1) + 1):

            # dp[0] represents the state where we only use characters from s1.
            dp[0] = (dp[0] and s1[i - 1] == s3[i - 1])

            for j in range(1, len(s2) + 1):

                # dp[j] before updating = value from above.
                from_s1 = (dp[j] and s1[i - 1] == s3[i + j - 1])

                # dp[j - 1] after updating = value from the left.
                from_s2 = (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

                dp[j] = from_s1 or from_s2

        return dp[-1]


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    result = solution.isInterleave(s1, s2, s3)
    print(result)  # Expected output: True


# I use dynamic programming. I define `dp[i][j]` as whether the first `i` characters of `s1` and the first `j` characters of `s2` can form the first `i + j` characters of `s3`. 
# At every state, I have two choices. I can take the next character from `s1` if it matches the corresponding character in `s3` and the previous state `dp[i-1][j]` is true. 
# Or I can take it from `s2` if it matches and `dp[i][j-1]` is true. If either choice works, the current state is true. 
# I also first check that the lengths of `s1` and `s2` add up to the length of `s3`. 
# The 2D solution takes O(mn) time and O(mn) space, and we can optimize the space to O(min(m,n)).

# # ---
# # OR
# from typing import List

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         # Check Length
#         # Every character from s1 and s2 must be used to create s3.
#         if len(s1) + len(s2) != len(s3):
#             return False

#         # Create DP Table
#         # dp[i][j] means:
#         # Can we create the first i + j characters of s3 using the first i characters
#         # of s1 and the first j characters of s2?
#         dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

#         # Base Case
#         # Empty s1 and empty s2 can create an empty s3.
#         dp[0][0] = True

#         # Fill DP Table
#         for i in range(len(s1) + 1):

#             for j in range(len(s2) + 1):

#                 # Skip the starting cell.
#                 if i == 0 and j == 0:
#                     continue

#                 # Take Character From s1
#                 if i > 0:
#                     if (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]):
#                         dp[i][j] = True

#                 # Take Character From s2
#                 if j > 0:
#                     if (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]):
#                         dp[i][j] = True

#         # The final cell tells us whether the entire s3 can be formed.
#         return dp[len(s1)][len(s2)]