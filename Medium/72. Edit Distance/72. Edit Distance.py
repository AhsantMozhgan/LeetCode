# https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        dp = list(range(n + 1))

        for i in range(1, m + 1):
            previous_diagonal = dp[0]
            dp[0] = i

            for j in range(1, n + 1):
                current = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = previous_diagonal

                else:

                    insert = dp[j - 1] + 1

                    delete = dp[j] + 1

                    replace = previous_diagonal + 1

                    dp[j] = min(insert, delete, replace)

                previous_diagonal = current

        return dp[n]

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    word1 = "horse"
    word2 = "ros"
    result = solution.minDistance(word1, word2)
    print(result)  # Expected output: 3 (horse -> ros: replace h->r, delete e, delete s)


# I use dynamic programming. I define `dp[i][j]` as the minimum number of operations needed to convert the first `i` characters of `word1` into the first `j` characters of `word2`. 
# If the current characters are equal, no operation is needed, so I take the diagonal value. 
# Otherwise, I consider three operations: insert, delete, and replace. Insert comes from `dp[i][j-1]`, delete comes from `dp[i-1][j]`, and replace comes from `dp[i-1][j-1]`. 
# I add one operation to each and take the minimum. The base cases represent converting an empty string into a prefix using insertions, or a prefix into an empty string using deletions. 
# The time complexity is O(mn), and the 2D solution uses O(mn) space.


# ---
# OR
# from typing import List

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:

#         # Get String Lengths
#         m = len(word1)
#         n = len(word2)


#         # -----------------------
#         # Create DP Table
#         # -----------------------
#         #
#         # dp[i][j] represents the
#         # minimum number of operations
#         # needed to convert the first
#         # i characters of word1 into
#         # the first j characters of word2.
#         #
#         dp = [
#             [0] * (n + 1)
#             for _ in range(m + 1)
#         ]


#         # -----------------------
#         # Base Case: Empty word1
#         # -----------------------
#         #
#         # To convert an empty string
#         # into j characters, we need
#         # j insertions.
#         #
#         for j in range(n + 1):
#             dp[0][j] = j


#         # -----------------------
#         # Base Case: Empty word2
#         # -----------------------
#         #
#         # To convert i characters
#         # into an empty string, we need
#         # i deletions.
#         #
#         for i in range(m + 1):
#             dp[i][0] = i


#         # -----------------------
#         # Fill DP Table
#         # -----------------------
#         #
#         for i in range(1, m + 1):

#             for j in range(1, n + 1):

#                 # -----------------------
#                 # Characters Match
#                 # -----------------------
#                 #
#                 if word1[i - 1] == word2[j - 1]:

#                     # No operation is needed.
#                     #
#                     dp[i][j] = dp[i - 1][j - 1]


#                 # -----------------------
#                 # Characters Do Not Match
#                 # -----------------------
#                 #
#                 else:

#                     # Insert a character
#                     #
#                     insert = dp[i][j - 1] + 1


#                     # Delete a character
#                     #
#                     delete = dp[i - 1][j] + 1


#                     # Replace a character
#                     #
#                     replace = dp[i - 1][j - 1] + 1


#                     # Choose the operation
#                     # with the minimum cost.
#                     #
#                     dp[i][j] = min(
#                         insert,
#                         delete,
#                         replace
#                     )


#         # Return the minimum number
#         # of operations.
#         #
#         return dp[m][n]


# # Example Usage
# if __name__ == "__main__":
#     solution = Solution()
#     word1 = "horse"
#     word2 = "ros"
#     result = solution.minDistance(word1, word2)
#     print(result)  # Expected output: 3 (horse -> ros: replace h->r, delete e, delete s)
