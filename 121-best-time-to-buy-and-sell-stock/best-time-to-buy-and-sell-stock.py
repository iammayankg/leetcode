class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        N = len(prices)
        profit = 0

        for i in range(1, N):
            profit = max(profit, prices[i] - minSoFar)
            minSoFar = min(minSoFar, prices[i])
        return profit
        