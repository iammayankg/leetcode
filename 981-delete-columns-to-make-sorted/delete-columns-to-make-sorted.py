class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs[0])
        n = len(strs)
        count = 0
        for i in range(N):
            for j in range(1, n):
                if strs[j][i] < strs[j-1][i]:
                    count += 1
                    break
        return count


        