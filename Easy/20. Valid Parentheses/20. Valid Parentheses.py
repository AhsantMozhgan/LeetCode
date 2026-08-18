# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        # We use a stack to store opening brackets.
        # The last opening bracket must be closed first.
        stack = []

        # This dictionary tells us which opening bracket belongs to each closing bracket.
        bracket_pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Go through the string from left to right.
        for current_character in s:

            # If the character is an opening bracket, put it into the stack.
            if current_character in "([{":
                stack.append(current_character)

            # Otherwise, we have a closing bracket.
            # We need to make sure:
            # 1. There is an opening bracket to match it.
            # 2. The opening bracket is the correct type.
            else:

                # If the stack is empty, there is no opening bracket for this closing bracket.
                if not stack:
                    return False

                # Get the most recently opened bracket.
                top_bracket = stack.pop()


                # Check whether the opening bracket matches the current closing bracket.
                if top_bracket != bracket_pairs[current_character]:
                    return False

        # If the stack is empty, every opening bracket was correctly closed.
        return len(stack) == 0

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.isValid("()[]{}"))    # Output: True
    print(solution.isValid("(]"))        # Output: False
    print(solution.isValid("([)]"))      # Output: False
    print(solution.isValid("{[]}"))      # Output: True
    print(solution.isValid("([{}])"))    # Output: True
    print(solution.isValid("]"))         # Output: False
    print(solution.isValid(""))           # Output: True (empty string is valid)


# I use a stack because brackets follow a last-in, first-out pattern. Whenever I see an opening bracket, I push it onto the stack. When I see a closing bracket, 
# I check the most recently opened bracket by popping the stack. If the brackets don't match, I return false. I also return false if I encounter a closing bracket while the stack is empty. 
# At the end, the stack must be empty, otherwise there are unmatched opening brackets.

# ---

# I use a stack because valid brackets follow a last-in, first-out order. 
# For example, if I open a parenthesis and then open a square bracket, I must close the square bracket before I can close the parenthesis.

# I walk through the string one character at a time.  
# Whenever I see an opening bracket — `(`, `[`, or `{` — I push it onto the stack.

# When I see a closing bracket I first check whether the stack is empty.  
# If it is, there is no matching opening bracket available, so the string is invalid.

# Otherwise I pop the most recent opening bracket and use a dictionary to verify that it matches the type of the current closing bracket.  
# If the types do not match I return false immediately.

# After processing the entire string the stack must be empty.  
# Any remaining brackets mean some openings never received their matching closings, so the string is invalid.

# OR
# class Solution:
#     def isValid(self, s: str) -> bool:

#         matching_brackets = {
#             ")": "(",
#             "]": "[",
#             "}": "{"
#         }

#         open_brackets = []  # Stack to keep track of open brackets

#         for current_character in s:

#             if current_character not in matching_brackets:
#                 # If it's an opening bracket, push it onto the stack
#                 open_brackets.append(current_character)

#             else:
#                 # Check if the stack is empty or the top of the stack doesn't match
#                 if (
#                     not open_brackets
#                     or open_brackets[-1] != matching_brackets[current_character]
#                 ):
#                     return False  # Invalid if there's a mismatch

#                 open_brackets.pop()  # Pop the matched opening bracket

#         # If the stack is empty, all brackets matched, return true
#         return len(open_brackets) == 0

