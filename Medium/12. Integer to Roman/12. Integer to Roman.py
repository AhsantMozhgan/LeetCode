# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of integers to Roman numeral symbols
        int_to_roman = (
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        )

        result = ""

        # Loop through the value-symbol pairs
        for value, symbol in int_to_roman:
            # While num is greater than or equal to the value
            while num >= value:
                result += symbol  # Append the Roman numeral
                num -= value      # Subtract the value from num

        return result



# I use a greedy approach. I store the Roman numeral values and their symbols in descending order, starting from the largest. I also include the special subtractive pairs—CM for 900, CD for 400, XC for 90, IX for 9, and so on—right in that list.

# Then I walk through each value-symbol pair. While the remaining number is still at least as large as the current value, I append the corresponding symbol to the result and subtract that value from the number.

# Because the subtractive pairs are already in the mapping, they get handled automatically. For example, with 1994 I take one M, then CM, then XC, then IV, which produces MCMXCIV.

# Under the problem’s fixed input range this runs in O(1) time and O(1) extra space—the mapping has a constant number of entries and any Roman numeral has a bounded maximum length.
