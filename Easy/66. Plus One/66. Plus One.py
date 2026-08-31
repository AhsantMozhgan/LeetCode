# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Start From The End
        # We start with the last digit because adding 1 affects the rightmost digit first.
        for i in range(len(digits) - 1, -1, -1):

            # Check For 9
            # If the current digit is not 9, we can simply increase it by 1.
            if digits[i] < 9:

                digits[i] += 1

                # No carry remains, so we are done.
                return digits

            # Handle 9
            # If the digit is 9, adding 1 creates a carry.
            # Example:
            # 9 + 1 = 10
            # So the current digit becomes 0, and the carry moves to the digit on the left.
            digits[i] = 0

        # All Digits Were 9
        # If we reach this point, every digit was 9.
        # Example:
        # [9, 9, 9]
        # became:
        # [0, 0, 0]
        # We still have a carry of 1.
        # So we need to add 1 at the beginning.
        return [1] + digits


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    digits = [1, 2, 3]  # Example input
    result = solution.plusOne(digits)
    print(result)  # Expected output: [1, 2, 4]

    digits = [9, 9, 9]  # Another example input
    result = solution.plusOne(digits)
    print(result)  # Expected output: [1, 0, 0, 0]

# I process the digits from right to left because adding one affects the least significant digit first. 
# If the current digit is less than 9, I increment it and return immediately because there is no carry. 
# If the digit is 9, I set it to 0 and continue to the left because the carry needs to propagate. 
# If all digits are 9, they all become zero, so I return a new array with 1 at the beginning. 
# Why do you iterate from right to left?
# Because addition starts from the least significant digit, so any carry needs to propagate from right to left.
