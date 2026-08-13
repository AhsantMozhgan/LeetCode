# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            # Skip characters that are not letters or numbers.
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters ignoring uppercase/lowercase.
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers toward the center.
            left += 1
            right -= 1

        return True

# I’d use a two-pointer approach. One pointer starts at the beginning of the string and the other starts at the end.  

# Because the problem ignores spaces, punctuation, and case, I first advance each pointer inward until it lands on an alphanumeric character. Then I compare the two characters after converting them to lowercase.  

# If they don’t match I return false immediately. If they do match, I move both pointers inward and continue.  

# If the pointers cross without finding any mismatch, the string is a valid palindrome.  

# This way I never create a cleaned copy of the string, so the solution runs in O(n) time and uses only O(1) extra space.
