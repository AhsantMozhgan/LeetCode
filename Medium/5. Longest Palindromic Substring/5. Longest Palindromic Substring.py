# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Handle Small Input
        if len(s) < 2:
            return s

        # Store the boundaries of the longest palindrome.
        start = 0
        end = 0

        # Expand Around Center
        def expand(left: int, right: int) -> int:

            # Expand while the characters on both sides are equal.
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1

            # Return the length of the palindrome we found.
            return right - left - 1

        # Try Every Center
        for i in range(len(s)):

            # Odd-length palindrome
            odd_length = expand(i, i)

            # Even-length palindrome
            even_length = expand(i, i + 1)

            # Find the longer palindrome centered around i.
            current_length = max(odd_length, even_length)

            # Update Best Answer
            if current_length > end - start + 1:

                start = i - (current_length - 1) // 2

                end = i + current_length // 2


        # Return the longest palindrome.
        return s[start:end + 1]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(solution.longestPalindrome("cbbd"))   # Output: "bb"
    print(solution.longestPalindrome("a"))      # Output: "a"
    print(solution.longestPalindrome("ac"))     # Output: "a" or "c"
    
# I use the expand-around-center approach. A palindrome can have either one center character for odd length palindromes or two center characters for even length palindromes. 
# For every index, I try both types of centers and expand left and right while the characters are equal. 
# When the expansion stops, I calculate the palindrome length and update the longest one if necessary. 
# This avoids checking every substring explicitly. The time complexity is O(n²) and the extra space is O(1).


# # ---
# # OR
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expand_around_center(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             # Return the palindrome found
#             return s[left + 1:right]  # left + 1 because the left index is now one step back

#         longest_palindrome = ""
        
#         for i in range(len(s)):
#             # Odd length palindromes (single character center)
#             palindrome_odd = expand_around_center(i, i)
#             # Even length palindromes (two character center)
#             palindrome_even = expand_around_center(i, i + 1)
            
#             # Update longest palindrome if a longer one is found
#             if len(palindrome_odd) > len(longest_palindrome):
#                 longest_palindrome = palindrome_odd
#             if len(palindrome_even) > len(longest_palindrome):
#                 longest_palindrome = palindrome_even
                
#         return longest_palindrome