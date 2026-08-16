# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = dict()
        t_to_s = dict()

        for source_character, target_character in zip(s, t):
        # OR
        # for i in range(len(s)):

        #     source_character = s[i]
        #     target_character = t[i]

            # Check mapping from s to t.
            if source_character in s_to_t:
                if s_to_t[source_character] != target_character:
                    return False
            else:
                s_to_t[source_character] = target_character

            # Check mapping from t to s.
            if target_character in t_to_s:
                if t_to_s[target_character] != source_character:
                    return False
            else:
                t_to_s[target_character] = source_character

        return True


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.isIsomorphic("egg", "add"))    # Output: True
    print(solution.isIsomorphic("foo", "bar"))    # Output: False
    print(solution.isIsomorphic("paper", "title")) # Output: True


# Two strings are isomorphic when there is a consistent one-to-one mapping from characters in `s` to characters in `t`. 
# The same character in `s` must always map to the same character in `t`, and two different characters in `s` cannot map to the same character in `t`.  

# I enforce both directions of that relationship with two hash maps: one from `s` → `t` and one from `t` → `s`.  

# I walk through both strings together with `zip`. For each pair of characters:  
# - I first check whether the source character has already been mapped to a *different* target; if it has, I return false.  
# - Then I do the reverse check: if the target character is already mapped from a *different* source, I also return false.  

# If neither conflict occurs I store the pair in both maps.  
# If I finish the loop without finding any conflicts, the strings are isomorphic and I return true.  

# For example, `"egg"` and `"add"` are isomorphic because `e → a` and `g → d` stay consistent.  
# `"foo"` and `"bar"` are not, because `o` would have to map to both `a` and `r`.  

# The solution is O(n) time (a single pass) and O(k) space, where k is the number of distinct characters stored in the map


# OR
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         noRepeat = set()
#         pattern = dict()

#         for index, ch in enumerate(s):
#             if ch in pattern:
#                 if t[index] != pattern[ch]:
#                     return False
                
#             else:
#                 if t[index] in noRepeat:
#                     return False
#                 pattern[ch] = t[index]
#                 noRepeat.add(t[index])
#         return True
