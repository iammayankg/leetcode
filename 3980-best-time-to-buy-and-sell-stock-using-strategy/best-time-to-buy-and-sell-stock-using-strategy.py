class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        N = len(prices)
        pnlSum = [0] * (N+1)
        sellSum = [0] * (N+1)

        currPnL = 0
        currPr = 0
        for i in range(N):
            p = prices[i]
            s = strategy[i]
            currPr += p
            currPnL += s*p
            pnlSum[i+1] = currPnL
            sellSum[i+1] = currPr

        result = pnlSum[N]

        for i in range(k-1, N):
            sellPr = sellSum[i + 1] - sellSum[i-k//2+1]
            holdL = pnlSum[i-k+1] + pnlSum[N] - pnlSum[i+1]
            result = max(result, sellPr + holdL)
        return result
        