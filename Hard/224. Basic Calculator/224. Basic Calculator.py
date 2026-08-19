# https://leetcode.com/problems/basic-calculator

class Solution:
    def calculate(self, s: str) -> int:

        # Stores the number we are currently building.
        current_number = 0

        # Tells us whether the current number should be added or subtracted.
        # 1 means positive, -1 means negative
        current_sign = 1

        # Stores the result of the current level of the expression.
        current_result = 0

        # The stack stores the result and sign from before entering a parenthesis.
        stack = []

        # Process Every Character
        for current_character in s:

            # Build the complete number.
            if current_character.isdigit():
                current_number = (current_number * 10 + int(current_character))

            # The number we have just built should be added.
            elif current_character == "+":
                current_result += (current_sign * current_number)

                # The next number is positive.
                current_sign = 1

                # Reset the number.
                current_number = 0

            # The number we have just built should be subtracted.
            elif current_character == "-":
                current_result += (current_sign * current_number)

                # The next number is negative.
                current_sign = -1

                # Reset the number.
                current_number = 0

            # We are entering a new expression. Before entering it, save:
            # 1. The result so far
            # 2. The sign before the "("
            elif current_character == "(":

                # Save the result from before the parenthesis.
                stack.append(current_result)

                # Save the sign that should be applied to the result inside the parenthesis.
                stack.append(current_sign)

                # Start a fresh calculation inside the parenthesis.
                current_result = 0
                current_sign = 1

            # We have finished calculating the expression inside the parenthesis.
            elif current_character == ")":

                # First, add the last number inside the parenthesis.
                current_result += (current_sign * current_number)

                # Reset current number.
                current_number = 0

                # The last item in the stack is the sign that appeared before the "(".
                previous_sign = stack.pop()

                # The item before the sign is the result from before entering the parenthesis.
                previous_result = stack.pop()

                # Combine the expression inside the parenthesis with the previous result.
                current_result = (previous_result + previous_sign * current_result)

                # After closing the parenthesis, the result is already complete.
                # The sign outside the parenthesis is reset to positive.
                current_sign = 1

        # There may be a number at the end of the string that has not yet been added.
        current_result += (current_sign * current_number)

        # Return the final result.
        return current_result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.calculate("1 + 1"))                   # Output: 2
    print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))     # Output: 23
    print(solution.calculate("2-(5-6)"))                   # Output: 3
    print(solution.calculate("-(2+(3-(4-(5))))"))         # Output: -3

    
# I scan the expression from left to right. I keep track of the current number, its sign, and the result at the current parenthesis level. 
# When I see an opening parenthesis, I push the current result and sign onto a stack and start a new calculation. 
# When I see a closing parenthesis, I finish the current calculation, pop the previous result and sign, and combine them with the result inside the parentheses.

# ---
# I evaluate the expression in a single left-to-right pass. Because we only have addition, subtraction, and parentheses, I don’t need to worry about multiplication or division precedence.

# I keep three pieces of state:  
# - `current_number` – the multi-digit number I’m currently building,  
# - `current_sign` – whether that number should be added or subtracted,  
# - `current_result` – the running total at the current parenthesis level.

# When I see a digit I build the number the usual way: multiply the existing value by ten and add the new digit.  

# When I see a plus or minus I first apply the number I just finished (using its saved sign) to the running result. Then I update the sign for the next number and reset `current_number` to zero.

# Parentheses create a nested context.  
# At an opening parenthesis I push the result I’ve accumulated so far and the sign that precedes the parenthesis onto a stack. Then I reset the result and sign so I can evaluate the expression inside independently.

# At a closing parenthesis I first finish the last number that was inside the parentheses. I pop the saved sign and the previous result, multiply the parenthesized result by that saved sign, and add it back to the outer result. This correctly handles cases such as `1 - (2 + 3)`, where the minus applies to the entire parenthesized sub-expression.

# Finally, after the loop I still need to apply the last number, because there may not be a trailing operator that would have triggered that update.
