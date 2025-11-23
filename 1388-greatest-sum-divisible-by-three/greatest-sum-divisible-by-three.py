class Solution:
    def maxSumDivThree2(self, nums: List[int]) -> int:
        a = sorted([num for num in nums if num % 3 == 0])
        b = sorted([num for num in nums if num % 3 == 1])
        c = sorted([num for num in nums if num % 3 == 2])

        total = sum(nums)
        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            ret = 0
            if b:
                ret = max(ret, total - b[0])
            if len(c) >= 2:
                ret = max(ret, total - c[0]-c[1])
            return ret
        else:
            ret = 0
            if c:
                ret = max(ret, total - c[0])
            if len(b) >= 2:
                ret = max(ret, total - b[0] - b[1])
            return ret

    def maxSumDivThree(self, nums: List[int]) -> int:
        return self.maxSumDivThree2(nums)
        N = len(nums)
        @cache
        def dp(index, mod):
            if index == N:
                return 0 if mod == 0 else -10**9
            new_mod = (mod + nums[index])%3
            #take
            res1 = nums[index] + dp(index+1, new_mod)
            #skip
            res2 = dp(index+1, mod)
            return max(res1, res2)
        return dp(0, 0)

        