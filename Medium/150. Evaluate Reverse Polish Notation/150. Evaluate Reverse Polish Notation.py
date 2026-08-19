# https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # The stack stores numbers that are waiting to be used in an operation.
        stack = []

        # A token can be either: 1. A number 2. An operator
        for current_token in tokens:

            # If the token is a number, convert it to an integer and push it onto the stack.
            if current_token not in {"+", "-", "*", "/"}:
                stack.append(int(current_token))

            # If the token is an operator, we need the last two numbers from the stack.
            else:

                # The first number we pop is the RIGHT operand.
                right_operand = stack.pop()

                # The second number we pop is the LEFT operand.
                left_operand = stack.pop()

                # Perform Operation
                if current_token == "+":
                    result = left_operand + right_operand

                elif current_token == "-":
                    result = left_operand - right_operand

                elif current_token == "*":
                    result = left_operand * right_operand

                else:
                    # Division must truncate toward zero. int() gives us truncationtoward zero.
                    result = int(left_operand / right_operand)

                # Put the result back onto the stack.
                stack.append(result)

        # After processing all tokens, only one number should remain.
        return stack[-1]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))      # Output: 9
    print(solution.evalRPN(["4", "13", "5", "/", "+"]))     # Output: 6
    print(solution.evalRPN(["10", "6", "9", "3", "/", "-"])) # Output: 10
    print(solution.evalRPN(["10", "6", "9", "3", "/", "-", "*"])) # Output: -60


# I use a stack to evaluate the expression from left to right. If the token is a number, I push it onto the stack. 
# If it is an operator, I pop the top two numbers, where the first popped value is the right operand and the second is the left operand. 
# I apply the operator and push the result back onto the stack. After processing all tokens, the stack contains exactly one value, which is the answer.

# ---
# Reverse Polish Notation places the operator after its operands, so a stack is a natural fit. The stack simply holds numbers that are waiting to be used by a later operator.

# I scan the tokens from left to right.  
# Whenever I see a number I convert it to an integer and push it onto the stack.

# Whenever I see an operator I pop the top two values.  
# The first value I pop is the right operand and the second is the left operand — that order matters for subtraction and division.  
# For example, the tokens `["4", "13", "5", "/"]` mean 13 ÷ 5, not 5 ÷ 13.

# I apply the operator to the left and right operands and push the result back onto the stack.  

# When I finish processing every token, all intermediate expressions have been reduced, so the single remaining value on the stack is the final answer.

# For division I use `int(left / right)` because the problem requires truncation toward zero. Python’s floor-division operator `//` cannot be used directly, since it behaves differently with negative numbers.
