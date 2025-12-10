class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        min_complexity = min(complexity)
        if complexity.count(min_complexity) != 1 or complexity[0] != min_complexity:
            return 0
        N = len(complexity)
        MOD = 10**9 + 7
        res = 1
        for i in range(2, N):
            res = res * i
            res = res % MOD

        return res
        