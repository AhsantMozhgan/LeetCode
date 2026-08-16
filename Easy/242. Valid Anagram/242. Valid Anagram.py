# https://leetcode.com/problems/valid-anagram

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
        # OR
        # return sorted(s) == sorted(t)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.isAnagram("anagram", "nagaram"))  # Output: True
    print(solution.isAnagram("rat", "car"))          # Output: False


# Two strings are anagrams if they contain exactly the same characters with the same frequencies, just possibly in a different order.  

# First I compare their lengths. If the lengths differ they can’t be anagrams, so I return false immediately.  

# When the lengths match I build a frequency map for each string—Python’s `Counter` makes this easy. For example, `"anagram"` produces 
# the counts three `'a'`s, one `'n'`, one `'g'`, one `'r'`, and one `'m'`.  

# If the two frequency maps are identical, every character appears the same number of times in both strings, so I return true; otherwise I return false.  

# The solution is O(n) time because I scan each string once. 
# Extra space is O(k) where k is the number of distinct characters; for lowercase English letters that is effectively O(1).
