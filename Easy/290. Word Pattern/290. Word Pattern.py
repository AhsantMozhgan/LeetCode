# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # If the number of unique characters does not match the number of words
        if len(pattern) != len(words):
            return False
        
        # Mappings from pattern to words and vice versa
        pattern_to_word = dict()
        word_to_pattern = dict()
        
        for pattern_character, current_word in zip(pattern, words):
            if pattern_character in pattern_to_word:
                # Check if the current mapping is consistent
                if pattern_to_word[pattern_character] != current_word:
                    return False
            else:
                pattern_to_word[pattern_character] = current_word
            
            if current_word in word_to_pattern:
                # Check if the current mapping is consistent
                if word_to_pattern[current_word] != pattern_character:
                    return False
            else:
                word_to_pattern[current_word] = pattern_character
        
        return True

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.wordPattern("abba", "dog cat cat dog"))  # Output: True
    print(solution.wordPattern("abba", "dog cat cat fish"))  # Output: False
    print(solution.wordPattern("aaaa", "dog cat cat dog"))   # Output: False



# I start by splitting the input string into words. If the number of words doesn’t match the number of characters in the pattern, 
# it can’t follow the pattern, so I return false right away.  

# The key requirement is a one-to-one mapping between pattern characters and words.  
# For example, if `'a'` maps to `"dog"`, every later `'a'` must also map to `"dog"`, and no other character is allowed to map to `"dog"`.  

# To enforce that bijection I keep two dictionaries:  
# - `pattern_to_word` makes sure each pattern character always maps to the same word,  
# - `word_to_pattern` makes sure a word is never assigned to more than one pattern character.  

# I then walk through the pattern and the words together. For each pair I check whether either direction already has a conflicting mapping. 
# If it does, I return false. Otherwise I store the new mapping in both dictionaries.  

# If I finish the loop without finding any conflict, the string follows the pattern and I return true.  

# For example, `"abba"` and `"dog cat cat dog"` return true, while `"abba"` and `"dog cat cat fish"` return false 
# because `'a'` would have to map first to `"dog"` and later to `"fish"`.  

# The whole solution is a linear scan and uses hash maps to maintain the required bijection.



# OR
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         patternDict = dict()
#         sDict = dict()

#         sList = s.split(" ")

#         for index, word in enumerate(sList):
#             letter = pattern[index]

#             if letter in patternDict:
#                 if patternDict[letter] != word:
#                     return False
#             else:
#                 patternDict[letter] = word
                
            
#             if word in sDict:
#                 if word != patternDict[letter]:
#                     return False
        
#         return True
