import math
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return math.inf
            curr_min = math.inf
            for coin in coins:
                if coin <= remaining:
                    curr_min = min(curr_min, 1 + dp(remaining-coin))
            return curr_min
        
        ret = dp(amount)
        return ret if ret != math.inf else -1