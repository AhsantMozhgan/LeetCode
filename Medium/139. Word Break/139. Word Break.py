# https://leetcode.com/problems/word-break

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Store the words in a set for fast lookup.
        word_set = set(wordDict)

        # dp[i] means:
        # Can we break the first i characters of s into valid words?
        dp = [False] * (len(s) + 1)

        # An empty string can always be successfully segmented.
        dp[0] = True

        # Check Every Position
        for i in range(1, len(s) + 1):

            # Try every possible word ending at position i.
            for j in range(i):

                # s[j:i] is the substring we are currently checking.
                word = s[j:i]

                # We can break s[:i] if:
                # 1. s[:j] can be segmented
                # 2. s[j:i] is a valid word
                if dp[j] and word in word_set:
                    dp[i] = True
                    break       # No need to check further if we found a valid segmentation

        # The last position tells if the whole string can be segmented
        return dp[len(s)]


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    result = solution.wordBreak(s, wordDict)
    print(result)  # Expected output: True

# I use dynamic programming to determine whether the string can be segmented into valid dictionary words. 
# I define `dp[i]` as whether the first `i` characters can be successfully segmented. For every position `i`, I try every previous position `j`. 
# If `dp[j]` is true and the substring `s[j:i]` is in the dictionary, then `dp[i]` is true. I store the dictionary in a set so word lookups are efficient. 
# I initialize `dp[0]` to true because an empty prefix is a valid starting point. Finally, `dp[len(s)]` tells me whether the entire string can be segmented.
