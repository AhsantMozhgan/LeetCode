# https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if either string is empty
        if not s or not t:
            return ""

        # Create a counter for the characters in t
        need = Counter(t)

        # Initialize a dictionary to count characters in the current window
        window = dict()

        # Counters for unique characters that are currently in the window
        have = 0
        
        required = len(need)    # Total unique characters required

        left = 0    # Left pointer for the sliding window

        result = ""     # To store the result substring

        result_length = float('inf')    # Initialize result length to infinity

        # Iterate over the string with the right pointer
        for right in range(len(s)):
            char = s[right]
            # Add the current character to the window count
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1   # Increment have when the current char meets the need

            # When we have all required characters
            while have == required:
                current_length = right - left + 1   # Calculate the current window length

                # Update result if the current window is smaller than the previous best
                if current_length < result_length:
                    result_length = current_length
                    result = s[left:right + 1]  # Update the result substring

                # Remove the leftmost character from the window
                left_char = s[left]
                window[left_char] -= 1  # Decrease the count of the left character

                # If removing left_char causes a deficit, decrease have
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1  # Move the left pointer to shrink the window

        return result  # Return the minimum window substring


# I’d use a sliding window with two frequency maps.  
# `need` stores how many of each character from `t` the window must contain, and `window` stores the counts currently inside the window of `s`.  

# I also keep two counters: `required` (the number of distinct characters in `t`) and `have` (how many of those requirements are currently satisfied). 
# A character only increments `have` when its count in the window reaches exactly the count required by `t` — this correctly handles duplicates.  

# I expand the window by moving the right pointer and adding characters. As soon as `have == required`, the window contains every required character with sufficient frequency, 
# so it is valid. At that point I shrink it from the left as far as possible while it remains valid, updating the best (shortest) result whenever I find a better one.  

# When removing the leftmost character causes its count to fall below what `t` needs, I decrement `have` because the window is no longer valid, then continue expanding from the right.  

# Because both pointers only move forward through `s`, the solution runs in O(|s| + |t|) time and uses O(|s| + |t|) space in the worst case for the frequency maps.
