class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        dp = {}
        def dfs(i, chance, buying):
            if i == len(prices):
                return 0
            if chance == 0:
                return 0
            ck = (i, chance, buying)
            if ck in dp:
                return dp[ck]
            cd = dfs(i+1, chance, buying)
            if buying:
                dp[ck] = max(cd, dfs(i+1, chance, not buying) - prices[i])
            else:
                dp[ck] = max(cd, dfs(i+1, chance-1, True) + prices[i])
            return dp[ck]
        return dfs(0, k, True)

        