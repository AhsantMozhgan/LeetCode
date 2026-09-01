# https://leetcode.com/problems/letter-combinations-of-a-phone-number

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # If digits is empty, there are no combinations.
        if not digits:
            return []

        # Map each digit to its corresponding letters.
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Store all generated combinations.
        result = []

        # Backtracking
        # index:
        # Which digit are we currently processing?
        # current:
        # Combination built so far.
        def backtrack(index, current):

            # Base Case
            # If we have processed every digit, we have a complete combination.
            if index == len(digits):
                result.append(current)
                return

            # Get the current digit.
            digit = digits[index]

            # Get all letters that correspond to this digit.
            letters = phone[digit]

            # Try Every Letter
            for letter in letters:

                # Add the selected letter to the current combination.
                backtrack(index + 1, current + letter)

        # Start from the first digit with an empty combination.
        backtrack(0, "")

        # Return all combinations.
        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    result = solution.letterCombinations(digits)
    print(result)  # Expected output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


# I use backtracking to generate all possible combinations. I map each digit to its corresponding letters. 
# At each recursion level, I process one digit and try every letter associated with that digit. 
# I add the selected letter to the current combination and recursively process the next digit. 
# When the index reaches the end of the input, I add the completed combination to the result.
