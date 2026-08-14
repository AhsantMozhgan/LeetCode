# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen_characters = set()  # This set will store the characters in the current substring
        left = 0  # This is the left pointer for the sliding window
        longest_length = 0  # Variable to keep track of the longest substring length

        for right, val in enumerate(s):  # Right pointer iterating through the string
            # If the character at 'right' is already in the set, shrink from the left
            while val in seen_characters:
                # Remove the character at the left pointer from the set
                seen_characters.remove(s[left])  
                left += 1  # Move the left pointer to the right
                
            seen_characters.add(val)  # Add the current character at 'right' to the set
            
            # Update the longest length found so far
            longest_length = max(longest_length, right - left + 1)

        return longest_length  # Return the length of the longest substring found


# I’d use a sliding window with two pointers and a set to keep track of the characters currently in the window.  

# I move the right pointer forward one step at a time and try to add each new character to the set.  
# If the character is already in the set, I shrink the window from the left: I remove characters and advance the left pointer until that duplicate is gone.  

# After every move I update the maximum length I’ve seen so far, which is just `right - left + 1`.  

# Because every character is added to the set at most once and removed at most once, the whole algorithm runs in O(n) time.
