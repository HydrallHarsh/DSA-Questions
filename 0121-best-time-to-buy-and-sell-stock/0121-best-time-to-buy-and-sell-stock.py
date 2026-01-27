class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float("inf")
        max_profit = 0
        for price in prices:
            if (buy_price < price):
                max_profit = max(max_profit, (price - buy_price))
            else:
                buy_price = price
        return max_profit