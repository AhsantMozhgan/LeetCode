# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        # Single digit numbers are always palindromes
        if x < 10:
            return True
        
        # Convert the number to string and check for palindrome
        str_x = str(x)
        return str_x == str_x[::-1]


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    number = 121  # Example input
    result = solution.isPalindrome(number)
    print(result)  # Expected output: True

    number = -121  # Another example input
    result = solution.isPalindrome(number)
    print(result)  # Expected output: False

    number = 10  # Another example input
    result = solution.isPalindrome(number)
    print(result)  # Expected output: False


# I convert the integer to a string and compare the string with its reversed version. If they are equal, the number is a palindrome.


# # ---
# # OR
# class Solution:
#     def isPalindrome(self, x: int) -> bool:

#         # Negative Numbers
#         # Negative numbers cannot be palindromes. So return False.
#         if x < 0:
#             return False

#         # Numbers Ending With 0
#         # If a number ends with 0, its reverse would start with 0.
#         # Example:
#         # 10 -> 01
#         # As an integer:
#         # 01 = 1
#         # So 10 cannot be a palindrome.
#         # The only exception is 0 itself.
#         if x % 10 == 0 and x != 0:
#             return False

#         # Reverse Half
#         # reversed_half stores the reversed second half of the number.
#         reversed_half = 0

#         # Process Half
#         # Continue until the reversed half becomes greater than or equal to the remaining first half.
#         while x > reversed_half:

#             # Get Last Digit
#             # Extract the rightmost digit of x.
#             # Example:
#             # x = 1221
#             # x % 10 = 1
#             last_digit = x % 10

#             # Add Digit To Reverse
#             # Move reversed_half one decimal position to the left. Then add the new digit.
#             reversed_half = reversed_half * 10 + last_digit

#             # Remove Last Digit
#             # Remove the digit that we just processed.
#             x = x // 10

#         # Even Number Of Digits
#         # Example:
#         # 1221
#         # After processing:
#         # x = 12
#         # reversed_half = 12
#         # They should be equal.
#         if x == reversed_half:
#             return True

#         # Odd Number Of Digits
#         # Example:
#         # 12321
#         # After reversing half:
#         # x = 12
#         # reversed_half = 123
#         # The middle digit (3) does not matter.
#         # Remove it from reversed_half by dividing by 10.
#         return x == reversed_half // 10
        
# # I don't need to reverse the entire number. I reverse only the second half of the digits and compare it with the first half. 
# I repeatedly take the last digit using modulo 10, append it to the reversed half, and remove it from the original number using integer division by 10. 
# For an odd number of digits, I ignore the middle digit by dividing the reversed half by 10.

# #  Why only reverse half?
# # Because for a palindrome, the first half must match the reverse of the second half. Reversing the entire number would do unnecessary work.
