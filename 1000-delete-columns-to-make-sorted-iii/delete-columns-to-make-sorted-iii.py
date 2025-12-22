class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        dp = [1] * cols

        for i in range(cols-2, -1, -1):
            for j in range(i+1, cols):
                if all(row[i] <= row[j] for row in strs):
                    dp[i] = max(dp[i], dp[j]+1)
        return cols - max(dp)
        