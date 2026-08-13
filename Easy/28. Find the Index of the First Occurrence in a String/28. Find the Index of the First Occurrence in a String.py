# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # The empty string is considered to occur at index 0.
        if not needle:
        # if needle == "":
            return 0

        # We only need to check positions where
        # the entire needle can fit inside haystack.
        for start_index in range(len(haystack) - len(needle) + 1):

            # Check whether needle starts at this position.
            if haystack[start_index:start_index + len(needle)] == needle:
                return start_index

        # needle was not found.
        return -1


# I’d use a straightforward sliding-window approach.  

# First, if `needle` is empty I return 0, because an empty string is considered to occur at the beginning of any string.  

# Then I check every valid starting position in `haystack` where the full `needle` can still fit. At each position 
# I take a substring of the same length as `needle` and compare it directly with `needle`.  

# If they match, I return that starting index right away — since I’m scanning from left to right, it’s the first occurrence.  
# If I finish checking all possible positions without a match, I return -1.  

# If *n* is the length of `haystack` and *m* is the length of `needle`, the worst-case time is O((n − m + 1) · m), 
# usually written as O(nm), and it uses constant extra space aside from Python’s temporary slices.

# OR
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:

#         for index in range(len(haystack) - len(needle) + 1):
#             if needle == haystack[index: index + len(needle)]:
#                 return index

#         return -1
        