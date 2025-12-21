class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs[0])
        n = len(strs)
        res = 0
        isSorted = [False] * n
        for i in range(N):
            found_mismatch = False
            for j in range(1, n):
                if not isSorted[j] and strs[j][i] < strs[j-1][i]:
                    found_mismatch = True
            if found_mismatch is True:
                res += 1
                continue

            for j in range(1, n):
                if not isSorted[j] and strs[j][i] > strs[j-1][i]:
                    isSorted[j] = True
            if all(isSorted):
                break

        return res