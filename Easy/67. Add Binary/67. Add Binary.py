# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Initialize Pointers
        # Start from the rightmost character of both strings.
        i = len(a) - 1
        j = len(b) - 1

        # Carry
        # carry stores the value that needs to be carried to the next position. Initially there is no carry.
        carry = 0

        # Result
        # Store each calculated bit here.
        result = []

        # Process Both Strings
        # Continue while:
        # 1. a still has characters
        # 2. b still has characters
        # 3. OR there is still a carry
        while i >= 0 or j >= 0 or carry:

            # Calculate Current Sum
            # Start with the carry.
            current_sum = carry

            # If a still has a character, add its current binary digit.
            if i >= 0:
                current_sum += int(a[i])

            # If b still has a character, add its current binary digit.
            if j >= 0:
                current_sum += int(b[j])

            # Calculate Result Bit
            # Binary digits can only be: 0 or 1
            # current_sum % 2 gives us the current result bit.
            # Example:
            # current_sum = 2
            # 2 % 2 = 0
            # So current bit = 0
            result.append(str(current_sum % 2))

            # Calculate Carry
            # current_sum // 2 tells us whether we need to carry 1.
            # Example:
            # current_sum = 2
            # 2 // 2 = 1
            # carry = 1
            carry = current_sum // 2

            # Move Pointers
            # Move both pointers one position to the left.
            i -= 1
            j -= 1

        # Reverse Result
        # We processed the strings from right to left.
        # Therefore result is currently stored backwards.
        # Example:
        # Actual answer:
        # 10101
        # result currently contains:
        # ['1', '0', '1', '0', '1']
        # Actually this represents the bits from right to left.
        result.reverse()

        # Build Final String
        # Convert the list of characters into one string.
        return "".join(result)


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    a = "1010"  # Binary number 10 in decimal
    b = "1011"  # Binary number 11 in decimal
    result = solution.addBinary(a, b)
    print(result)  # Expected output: "10101" (binary for 21 in decimal)


# I treat the two binary strings like normal addition. I start from the rightmost digits using two pointers and maintain a carry. 
# For each position, I add the current bits and the carry. The result bit is `sum % 2`, and the new carry is `sum // 2`. 
# I continue while either string still has digits or there is a remaining carry. Since I build the result from right to left, I reverse it at the end.

# ---
# OR
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         # Initialize the result and carry
#         result = []
#         carry = 0
        
#         # Pointers for the end of both strings
#         i, j = len(a) - 1, len(b) - 1
        
#         # Loop until both strings are processed
#         while i >= 0 or j >= 0 or carry:
#             total = carry
            
#             if i >= 0:
#                 total += int(a[i])
#                 i -= 1
            
#             if j >= 0:
#                 total += int(b[j])
#                 j -= 1
            
#             carry = total // 2  # Calculate carry for next position
#             result.append(str(total % 2))  # Append the current bit to the result
        
#         # The result is built in reverse order
#         result.reverse()
        
#         # Join the list into a string and return
#         return ''.join(result)
