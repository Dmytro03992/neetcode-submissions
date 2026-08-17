class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 0
        ma = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                ma = max(ma, profit)
            else:
                b = s
            s += 1
        return ma