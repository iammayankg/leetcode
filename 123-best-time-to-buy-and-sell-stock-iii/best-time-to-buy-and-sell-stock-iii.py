from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(idx, buying, tx):
            if idx == len(prices) or tx == 0:
                return 0
            # if buy
            if buying:
                return max(-prices[idx] + dp(idx+1, not buying, tx), dp(idx+1, buying, tx))
            else:
                return max(prices[idx] + dp(idx+1, not buying, tx-1), dp(idx+1, buying, tx))
        return dp(0, True, 2)
        