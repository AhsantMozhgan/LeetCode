# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pointerS = 0
        lengthS = len(s)

        if lengthS == 0:
            return True

        for ch in t:
            if ch == s[pointerS]:
                pointerS += 1
                if pointerS >= lengthS:
                    return True

        return False



# I’d use a two-pointer approach. One pointer tracks the next character I still need to match in `s`, and I simply scan through every character in `t`.  

# Whenever the current character in `t` matches the character I’m looking for in `s`, I advance the pointer in `s`. Characters in `t` that don’t match are just skipped.  

# If the pointer reaches the end of `s`, that means every character of `s` was found in the correct order, so I return true. If I finish scanning `t` first, then `s` is not a subsequence.  

# I also handle the empty-string case up front, because an empty string is always a subsequence.  

# The whole solution runs in O(|t|) time and uses only O(1) extra space.
