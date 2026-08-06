# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        # Compare each day with the previous day.
        for current_day in range(1, len(prices)):

            # If the price goes up from the previous day, we can make a profit
            if prices[current_day] > prices[current_day - 1]:
                total_profit += prices[current_day] - prices[current_day - 1]
                
        return total_profit


# This solution uses a greedy approach for the version where multiple transactions are allowed, as long as I hold at most one share at a time.  

# I walk through the prices and compare each day with the previous day.  
# Whenever today’s price is higher, I add that difference to the total profit — it’s like buying yesterday and selling today.  

# If the price stays the same or goes down, I simply skip it because there’s no profit to capture.  

# Summing every positive consecutive difference is equivalent to buying at the start of each rising stretch
# and selling at the end of it, which gives the maximum possible profit.  

# The whole thing runs in O(n) time and uses only O(1) extra space.
