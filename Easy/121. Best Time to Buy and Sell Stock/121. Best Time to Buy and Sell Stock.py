# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        # Start with maximum possible value as initial minimum price.
        min_price = float('inf')  
        max_profit = 0  # Initialize maximum profit to 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price
            elif price - min_price > max_profit:
                # Update the maximum profit if we found a better option
                max_profit = price - min_price 
        
        return max_profit


# “I’d track the minimum price I’ve seen so far and the maximum profit I can make.  

# As I go through the prices, whenever I find a new lower price I update the minimum.  
# Otherwise I calculate the profit if I sold today — current price minus the 
# lowest price so far — and update the maximum profit if it’s better.  

# At the end, that maximum profit is the answer.  

# It runs in O(n) time and uses only O(1) extra space.”


# OR
# Time: O(n)
# Space: O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         buy = prices[0]

#         for i in range(1, len(prices)):
#             if prices[i] < buy:
#                 buy = prices[i]
#             else:
#                 profit = max(prices[i] - buy, profit)

#         return profit
