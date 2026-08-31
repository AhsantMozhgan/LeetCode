# https://leetcode.com/problems/factorial-trailing-zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:

        # This will store the total number of factors of 5.
        # Each factor of 5 can combine with a factor of 2 to create 10.
        zero_count = 0

        # Count Factors of 5
        # We repeatedly divide n by 5.
        # n // 5 counts numbers that contain at least one factor of 5.
        # n // 25 counts numbers that contain an additional factor of 5.
        # n // 125 counts another factor of 5, and so on.
        while n > 0:

            # Count how many multiples of the current power of 5 exist.
            n //= 5

            # Add how many multiples of 5
            zero_count += n

        # Return Answer
        return zero_count

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    n = 5  # Example input
    result = solution.trailingZeroes(n)
    print(result)  # Expected output: 1 (5! = 120 has one trailing zero)

    n = 10  # Another example input
    result = solution.trailingZeroes(n)
    print(result)  # Expected output: 2 (10! = 3628800 has two trailing zeros)

    n = 25  # Another example input
    result = solution.trailingZeroes(n)
    print(result)  # Expected output: 6 (25! has six trailing zeros)


# Trailing zeroes are created by factors of 10, and 10 is 2 times 5. Since factorials contain many more factors of 2 than factors of 5, the number of trailing zeroes is determined by the number of factors of 5. 
# I repeatedly divide n by 5 and add the result. This counts multiples of 5, then multiples of 25 for the extra factor of 5, then multiples of 125, and so on.
# Why don't you count factors of 2?
# Because there are always more factors of 2 than factors of 5 in a factorial, so 5 is the limiting factor.
