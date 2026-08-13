# https://leetcode.com/problems/reverse-words-in-a-string


class Solution:
    def reverseWords(self, s: str) -> str:

        # Split the string into words.
        # split() automatically removes extra spaces.
        words = s.split()

        # Reverse the order of the words.
        words.reverse()

        # Join the words with exactly one space between them.
        return " ".join(words)

# I’d use Python’s built-in string operations to handle both the word reversal and the extra spaces.  

# First I call `split()`, which breaks the string into a list of words and automatically strips all leading, trailing, and repeated spaces.  
# Then I reverse that list of words.  
# Finally I join them back together with a single space using `' '.join(words)`.  

# For example, `'  hello world  '` becomes `['hello', 'world']`, then `['world', 'hello']`, and finally `'world hello'`.  

# The whole solution runs in O(n) time and uses O(n) extra space, where n is the length of the input string.


# OR
# class Solution:
#     def reverseWords(self, s: str) -> str:

#         return " ".join(s.split()[::-1])
        