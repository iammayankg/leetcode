import math
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(idx, remaining):
            if remaining == 0:
                return 0
            if idx == len(coins):
                return math.inf
            
            curr_min = dp(idx + 1, remaining)
            if remaining >= coins[idx]:
                curr_min = min(curr_min, 1 + dp(idx, remaining-coins[idx]))
            return curr_min
        
        ret = dp(0, amount)
        return ret if ret != math.inf else -1