# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:

        # Mapping of Roman numeral characters to integers
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total_value = 0
        value_on_right = 0

        # Process the Roman numerals from right to left.
        for current_character in reversed(s):
            current_value = roman_values[current_character]

            # If the value on the right is larger, subtract the current value.
            if current_value < value_on_right:
                total_value -= current_value
            else:
                # Otherwise, add the current value.
                total_value += current_value

            # The current value will be the value on the right
            # when we process the next character.
            value_on_right = current_value

        return total_value


# I use a hash map to convert each Roman numeral character into its integer value, then I scan the string from right to left.

# Roman numerals normally add their values, but a smaller numeral placed before a larger one means subtraction—for example IV is 5 − 1 = 4.  
# By scanning from right to left I always know the value of the character immediately to the right.

# If the current value is smaller than the one on its right, I subtract it because it forms a subtractive pair.  
# Otherwise I simply add it. Then I update the “right-side” value for the next character.

# Take MCM as an example: I first add the rightmost M (1000), then subtract C because it is smaller than the M that follows it, 
# and finally add the leftmost M, giving 1000 − 100 + 1000 = 1900.

# The whole process is O(n) time and O(1) extra space, since the map contains only the seven fixed Roman symbols.
