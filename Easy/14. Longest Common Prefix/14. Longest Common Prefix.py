# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Iterate over the strings from the second to the last
        for string in strs[1:]:
            # Keep reducing the prefix until it matches the start of the current string
            while not string.startswith(prefix):
                # Reduce the prefix by one character
                prefix = prefix[:-1]
                if prefix == "":
                    return ""  # No common prefix
        
        return prefix


# I start by assuming the entire first string is the common prefix. Then I compare that prefix against every remaining string.  

# Whenever the current string does not begin with my prefix, I shorten the prefix by one character from the end and check again. 
# I keep shrinking it until it matches the start of the current string.  

# If the prefix ever becomes empty, I can return the empty string right away because there is no common prefix among all the strings.  

# After I’ve processed every string, whatever is left of the prefix is the longest one shared by all of them.  

# The worst-case time is O(S), where S is the total number of characters across all input strings, and the algorithm uses only O(1) extra space beyond the returned string.