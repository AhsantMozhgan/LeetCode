# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()  # To store the numbers we've encountered

        while n != 1:
            if n in seen_numbers:
                return False  # Cycle detected
            seen_numbers.add(n)  # Add the current number to the set

            # Calculate the sum of the squares of the digits
            current_sum = 0
            while n > 0:
                digit = n % 10
                current_sum += digit ** 2  # Square the digit and add to current_sum
                n = n // 10  # Remove the last digit from n

            n = current_sum  # Update n to the new value

        return True  # If we reach 1, return True

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.isHappy(19))  # Output: True
    print(solution.isHappy(2))   # Output: False

# A happy number is one that, when you repeatedly replace it with the sum of the squares of its digits, eventually reaches 1. 
# If it never does and instead falls into a cycle, it’s not happy.

# I use a set to keep track of every number I’ve already seen. On each step I first check whether the current number is already in the set. 
# If it is, I’ve detected a cycle, so I return false.

# If it’s new, I add it to the set and compute the next number: I repeatedly take the last digit with n % 10, square it, add it to a running sum, 
# and remove that digit with integer division. Then I replace n with that sum and continue.

# If n ever becomes 1, I return true. The set guarantees the loop always terminates, because the process either reaches 1 or repeats a previously seen value.
