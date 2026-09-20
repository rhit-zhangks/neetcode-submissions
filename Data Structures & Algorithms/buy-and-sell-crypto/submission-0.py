class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_sum = 0
        max_sum = 0
        buy_value = prices[0]
        for ind, price in enumerate(prices):
            curr_sum = price - buy_value
            if price - buy_value < 0:
                buy_value = price
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
            