class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows = len(strs)

        @cache
        def cur(last, i):
            if i == cols:
                return 0
            
            left = cur(last, i+1) + 1
            if last != -1:
                for j in range(rows):
                    if strs[j][last] > strs[j][i]:
                        return left
            return min(left, cur(i, i+1))
        return cur(-1, 0)
        