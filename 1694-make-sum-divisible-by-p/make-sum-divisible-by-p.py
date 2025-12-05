class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        currSum = 0
        total = sum(nums)
        total_mod = total%p
        if total_mod == 0:
            return 0

        dp = defaultdict(lambda: -math.inf)
        dp[0] = -1
        res = N
        for idx, num in enumerate(nums):
            currSum += num
            mod = currSum%p
            res = min(res, idx - dp[(mod-total_mod + p)%p])
            dp[mod] = idx


        return -1 if res == N else res
        