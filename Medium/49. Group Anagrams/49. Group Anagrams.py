# https://leetcode.com/problems/group-anagrams

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs:

            # Store the frequency of each letter a-z.
            character_counts = [0] * 26     # Assuming lowercase letters a-z

            for character in word:

                # Convert the character to an index from 0 to 25.
                index = ord(character) - ord('a')

                # Increase the frequency of this character.
                character_counts[index] += 1

            # Convert the list to a tuple to use as a key. so it can be used as a dictionary key.
            key = tuple(character_counts)

            # Add the word to the group with the same character counts.
            anagrams[key].append(word)

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test case
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# The key idea is that two strings are anagrams when they have exactly the same frequency for every letter.  

# Instead of sorting each word, I build a fixed-size array of 26 counts—one slot for every lowercase letter from `'a'` to `'z'`. 
# As I scan a character I convert it to an index with `ord(character) - ord('a')` and increment that position.  

# The finished count array becomes a unique signature for the word. So `"eat"`, `"tea"`, and `"ate"` all produce 
# the same signature because each contains one `'a'`, one `'e'`, and one `'t'`.  

# I turn the count list into a tuple (tuples are immutable and therefore hashable) and use that tuple as a key in a `defaultdict(list)`. 
# All words that share the same frequency signature end up in the same list.  

# Finally I just return the values of the dictionary—the anagram groups.
