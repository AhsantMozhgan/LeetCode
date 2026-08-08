# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)

        # Store the product of all elements to the left
        # of the current index.
        left_product = 1

        for current_index in range(len(nums)):

            answer[current_index] = left_product

            left_product *= nums[current_index]

        # Store the product of all elements to the right
        # of the current index.
        right_product = 1

        for current_index in range(len(nums) - 1, -1, -1):

            answer[current_index] *= right_product

            right_product *= nums[current_index]

        return answer



# For each index, the answer is the product of everything to its left multiplied by the product of everything to its right.  

# I use the output array itself to first store the left products. As I walk from left to right I keep a running `left_product`, and at each index I write the product of all values before that index.  

# Then I make a second pass from right to left with a running `right_product`. At each index I multiply the existing left product already in the answer array by the product of everything to its right.  

# After those two passes every position holds the product of all elements except itself.  

# This approach avoids division, handles zeros naturally, runs in O(n) time, and uses only O(1) extra space beyond the output array.