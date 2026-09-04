# https://leetcode.com/problems/coin-change

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Create DP Array
        # dp[i] represents the minimum number of coins needed to make the amount i.
        # We use amount + 1 as an "impossible" initial value.
        dp = [amount + 1] * (amount + 1)

        # Base Case
        # We need zero coins to make an amount of zero.
        dp[0] = 0

        # Build The DP Table
        for current_amount in range(1, amount + 1):

            # Try every available coin.
            for coin in coins:

                # We can use this coin only if it does not exceed the current amount.
                if coin <= current_amount:

                    # If we use this coin, we need one coin plus the best solution for the remaining amount.
                    dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

        # If dp[amount] was never updated, the amount cannot be formed.
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]  # Coin denominations
    amount = 11  # Target amount
    result = solution.coinChange(coins, amount)
    print(result)  # Expected output: 3 (11 can be made with 5 + 5 + 1)

# I use dynamic programming. I define `dp[i]` as the minimum number of coins needed to make amount `i`. 
# I initialize `dp[0]` to zero because no coins are needed to make zero. For every amount, I try every available coin. 
# If the coin is not larger than the current amount, I can use it and take the best solution for the remaining amount, which is `dp[current_amount - coin] + 1`. 
# I take the minimum over all possible coins. If the final value is still the initial impossible value, I return `-1`. 
# The time complexity is O(amount × number of coins), and the space complexity is O(amount).

# # ---
# # OR
# class Solution:
#     def coinChange(self, coins: list, amount: int) -> int:
#         # Initialize a DP array with infinity for all amounts except 0
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0  # Base case: 0 coins are needed to make the amount 0
        
#         # Iterate over each coin
#         for coin in coins:
#             for i in range(coin, amount + 1):
#                 dp[i] = min(dp[i], dp[i - coin] + 1)

#         # If dp[amount] is still infinity, it means we cannot make the amount
#         return dp[amount] if dp[amount] != float('inf') else -1
