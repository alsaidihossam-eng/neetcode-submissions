class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(len(prices) - i):
                current_profit = prices[i + j] - prices[i]
                if current_profit > max_profit:
                    max_profit = current_profit

        return max_profit