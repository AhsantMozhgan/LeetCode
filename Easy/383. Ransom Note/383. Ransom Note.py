# https://leetcode.com/problems/ransom-note

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the characters in the magazine
        magazine_count = Counter(magazine)
        
        # Check each character in the ransom note
        for char in ransomNote:
            if magazine_count[char] <= 0:
                return False
            magazine_count[char] -= 1  # Use one occurrence of the character
        
        return True

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.canConstruct("aa", "aab"))  # Output: True
    print(solution.canConstruct("aa", "ab"))   # Output: False


# I’d solve this by tracking how many of each character are available in the magazine.  

# First I build a frequency map of the magazine—using `Counter(magazine)` is convenient. 
# For example, if the magazine is `"aab"`, I know I have two `'a'`s and one `'b'`.  

# Then I walk through every character in the ransom note.  
# - If the character isn’t present in the map, or I’ve already used up all of its occurrences, I return false immediately.  
# - Otherwise I simply decrement its count to record that I’ve used one copy.  

# If I can process the entire ransom note without running out of any character, I return true.  

# The time complexity is O(m + n): one pass over the magazine to build the counts and one pass over the ransom note to validate it. 
# Extra space is O(k), where k is the number of distinct characters.
