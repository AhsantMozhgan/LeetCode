# https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:

        # Base Case
        # The square root of 0 or 1 is the number itself.
        if x < 2:
            return x

        # Search Range
        # For x >= 2, the answer is between 1 and x // 2.
        left = 1
        right = x // 2

        # Binary Search
        # Find the largest number whose square is <= x.
        while left <= right:

            # Find the middle of the current search range.
            mid = left + (right - left) // 2

            # Exact Square Root
            if mid * mid == x:
                return mid

            # Mid Is Too Small. We need a larger number.
            elif mid * mid < x:
                left = mid + 1

            # Mid Is Too Large. We need a smaller number.
            else:
                right = mid - 1

        # Return Integer Result
        # right is the largest number. whose square is smaller than x.
        return right

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    x = 4  # Example input
    result = solution.mySqrt(x)
    print(result)  # Expected output: 2

    x = 8  # Another example input
    result = solution.mySqrt(x)
    print(result)  # Expected output: 2 (since 2^2 = 4 and 3^2 = 9)
    
    x = 16  # Another example input
    result = solution.mySqrt(x)
    print(result)  # Expected output: 4


# I need to find the largest integer whose square is less than or equal to x. Since the square function is monotonically increasing for positive numbers, I can use binary search. 
# I check the middle value: if its square is too small, I search the right half; if its square is too large, I search the left half. 
# When the search ends, `right` is the largest valid integer, so I return it.

# Why do you return `right`?
# When the binary search finishes, `left` has moved to the first invalid value, while `right` is the last valid value whose square is less than or equal to x.



# ---
# # OR
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 2:
#             return x  # 0 and 1 are their own square roots
        
#         left, right = 2, x // 2  # Set initial bounds for binary search
        
#         while left <= right:
#             mid = (left + right) // 2  # Calculate mid point
#             square = mid * mid
            
#             if square == x:
#                 return mid  # Exact square root found
#             elif square < x:
#                 left = mid + 1  # Move right
#             else:
#                 right = mid - 1  # Move left
        
#         return right  # The floor of the square root


# ---
# # OR
# class Solution:
#     def mySqrt(self, x: int) -> int:
        # # Edge case: 0 and 1 are their own square roots
        # if x < 2:
        #     return x
        
        # # Start with an initial guess.
        # # Using 'x' itself works, but we can start with x // 2 for slight optimization.
        # guess = x
        
        # # Newton's formula: guess = (guess + x / guess) / 2
        # # We keep refining until guess^2 <= x (the floor sqrt).
        # while guess * guess > x:
        #     # Integer division is used here to keep the result as an integer
        #     # and automatically floor the value at each step.
        #     guess = (guess + x // guess) // 2
            
        # return guess
