class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        mem = {}

        def dp(index):
            if index == 0:
                return 1
            if index in mem:
                return mem[index]
            l = 1
            for j in range(index):
                if nums[j] < nums[index]:
                    l = max(l, 1 + dp(j))
            mem[index] = l
            return l

        return max(dp(i) for i in range(N))

        