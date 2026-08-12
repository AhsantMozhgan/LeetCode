# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        last_word_length = 0

        # Start from the last character and move left.
        for current_index in range(len(s) - 1, -1, -1):

            # Ignore spaces after the last word.
            if s[current_index] == " ":

                # If we already counted characters, we have reached the beginning of the last word.
                if last_word_length > 0:
                    break

            else:
                # Count the current character as part of the last word.
                last_word_length += 1

        return last_word_length


# I scan the string from right to left because I only care about the last word.  

# First I skip any trailing spaces.  
# As soon as I hit a non-space character I know I’ve reached the end of the last word, so I start counting.  
# I keep moving left, counting characters, until I either hit a space (the start of that word) or reach the beginning of the string.  

# The counter is then the length of the last word.  

# This runs in O(n) time in the worst case and uses only O(1) extra space.
