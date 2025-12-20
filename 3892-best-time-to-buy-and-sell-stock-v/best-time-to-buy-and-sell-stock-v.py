class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)
        BUYING = 0
        SELLING = 1
        NONE = 2
        dp = [[[-1]*3 for _ in range(k+1)] for _ in range(N+1)]

        # @cache
        def recurse(index, current_state, pending_transaction):
            if index == N or pending_transaction == 0:
                return 0 if current_state == NONE else -math.inf

            if dp[index][pending_transaction][current_state] != -1:
                return dp[index][pending_transaction][current_state]

            skip = recurse(index+1, current_state, pending_transaction)
            state0 = -math.inf
            if current_state == NONE:
                buy = -prices[index] + recurse(index+1, SELLING, pending_transaction)
                sell = prices[index] + recurse(index+1, BUYING, pending_transaction)
                state0 = max(buy, sell)
            elif current_state == BUYING:
                buy = -prices[index] + recurse(index+1, NONE, pending_transaction-1)
                state0 = buy
            else:
                state0 = prices[index] + recurse(index+1, NONE, pending_transaction-1)
            res = max(skip, state0)
            dp[index][pending_transaction][current_state] = res
            return res

        return recurse(0, NONE, k)
            
        