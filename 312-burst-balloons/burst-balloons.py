class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)

        @cache
        def dp(left, right):
            if left > right:
                return 0
            maxCost = 0
            for i in range(left, right+1):
                cost = nums[i] * nums[left-1] * nums[right+1]
                cost += dp(left, i-1) + dp(i+1, right)
                maxCost = max(maxCost, cost)
            return maxCost
        return dp(1, N-2)