# https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:

        # Every child must receive at least one candy.
        candies = [1] * len(ratings)

        # First pass:
        # Make sure every child with a higher rating than the child on the left gets more candies.
        for current_index in range(1, len(ratings)):

            if ratings[current_index] > ratings[current_index - 1]:
                candies[current_index] = candies[current_index - 1] + 1

        # Second pass:
        # Make sure every child with a higher rating than the child on the right gets more candies.
        for current_index in range(len(ratings) - 2, -1, -1):

            if ratings[current_index] > ratings[current_index + 1]:
                candies[current_index] = max(
                    candies[current_index],
                    candies[current_index + 1] + 1
                )

        return sum(candies)


# I use a greedy two-pass approach. Every child starts with one candy because each must receive at least one.

# In the first pass I go left to right. Whenever a child has a higher rating than the one on their left, I give them one more candy than that left neighbor. This satisfies the left-neighbor rule.

# In the second pass I go right to left. Whenever a child has a higher rating than the one on their right, they need more candies than that right neighbor. 
# I take the maximum of their current count and the right neighbor’s count plus one, so I never undo a larger value that was already assigned in the first pass.

# Finally I just sum the candy array. This gives the minimum number of candies that satisfy both neighbor constraints.  

# It runs in O(n) time and uses O(n) extra space.