class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(remaining):
            if remaining == 1:
                return 1
            if remaining == 2:
                return 2
            res = 0
            res += dp(remaining-1) + dp(remaining-2)
            return res
        return dp(n)