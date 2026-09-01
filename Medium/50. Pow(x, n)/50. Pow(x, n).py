# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Handle Negative Power
        # If n is negative:
        # x^(-n) = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n

        # Store The Result
        # Start with 1 because multiplying by 1 does not change the result.
        result = 1

        # Binary Exponentiation
        # Each iteration reduces n approximately by half.
        while n > 0:

            # Check If n Is Odd
            # If n is odd, we need to multiply the current x into our result.
            if n % 2 == 1:
                result *= x

            # Square x
            # Prepare x for the next power of two.
            x *= x

            # Divide n By 2
            # Integer division by 2 moves us to the next exponent level.
            n //= 2

        # Return Result
        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    x = 2.0  # Base
    n = 10   # Exponent
    result = solution.myPow(x, n)
    print(result)  # Expected output: 1024.0

    x = 2.1  # Base
    n = 3    # Exponent
    result = solution.myPow(x, n)
    print(result)  # Expected output: 9.261

    x = 2.0  # Base
    n = -2   # Negative exponent
    result = solution.myPow(x, n)
    print(result)  # Expected output: 0.25

# I use binary exponentiation instead of multiplying x n times. If n is odd, I multiply x into the result. 
# Then I square x and divide n by 2. This reduces the exponent by half at every iteration, giving us O(log n) time. 
# For a negative exponent, I take the reciprocal of x and make n positive.
#  Why is it O(log n)?
# Because I divide `n` by 2 after every iteration.
