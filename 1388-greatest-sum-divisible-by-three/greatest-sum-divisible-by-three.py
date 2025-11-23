class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
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

        