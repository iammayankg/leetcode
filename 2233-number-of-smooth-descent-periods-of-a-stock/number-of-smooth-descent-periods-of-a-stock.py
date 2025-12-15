class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 1
        cnt = 1
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff == -1:
                cnt += 1
            else:
                cnt = 1
            total += cnt
        # total += cnt
        return total


        