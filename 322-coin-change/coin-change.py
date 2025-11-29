class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        N = len(coins)
        
        @cache
        def dp(index, pending):
            if pending == 0:
                return 0
            if index == N:
                return math.inf if pending else 0
            ncoins = math.inf
            for i in range(index, N):
                if coins[i] > pending:
                    break
                ncoins = min(ncoins, 1 + dp(i, pending-coins[i]))
                
            return ncoins
        ncoins = dp(0, amount)
        return ncoins if ncoins < math.inf else -1
        