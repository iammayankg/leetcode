class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        N = len(nums)
        c = Counter(nums)
        maxNum = max(nums)

        @cache
        def recurse(n):
            if n == 0:
                return 0
            if n == 1:
                return c[1]

            return max(recurse(n-2) + n*c[n], recurse(n-1))
        return recurse(maxNum)
        