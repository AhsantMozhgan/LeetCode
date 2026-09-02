# https://leetcode.com/problems/generate-parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Store all valid parentheses strings.
        result = []

        # Backtracking
        # current:
        # The parentheses string built so far.
        # open_count:
        # Number of opening parentheses currently used.
        # close_count:
        # Number of closing parentheses currently used.
        def backtrack(current, open_count, close_count):

            # Base Case
            # A valid answer must contain exactly n opening and n closing parentheses.
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # Add Opening Parenthesis
            # We can add '(' as long as we have not used all n opening parentheses.
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()

            # Add Closing Parenthesis
            # We can add ')' only when there are unmatched '(' parentheses available.
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        # Start with an empty string and no parentheses used.
        backtrack([], 0, 0)

        # Return all valid combinations.
        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    n = 3  # Example with 3 pairs of parentheses
    result = solution.generateParenthesis(n)
    print(result)  # Expected output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

# I use backtracking to generate only valid parentheses strings. I keep track of how many opening and closing parentheses I've used. 
# I can add an opening parenthesis as long as I haven't used all `n` opening parentheses. 
# I can add a closing parenthesis only when the number of closing parentheses is smaller than the number of opening parentheses. 
# This guarantees that we never create an invalid prefix. When the current string reaches length `2 * n`, we have a valid solution and add it to the result.


# ---
# OR
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
        
#         results = []

#         def backtrack(current_string, open_count, close_count):
#             # If the current string has reached the maximum length
#             if len(current_string) == 2 * n:
#                 results.append(current_string)  # Save the valid combination
#                 return
            
#             # If we can add an open parenthesis
#             if open_count < n:
#                 backtrack(current_string + '(', open_count + 1, close_count)
            
#             # If we can add a close parenthesis
#             if close_count < open_count:
#                 backtrack(current_string + ')', open_count, close_count + 1)

#         backtrack('', 0, 0)  # Start with an empty string and counts for open and close parentheses
#         return results
