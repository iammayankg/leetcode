class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        nums.sort()
        slack = total % k

        ops = 0
        N = len(nums)
        for i in range(N-1, -1, -1):
            if nums[i] >= slack:
                ops += slack
                slack = 0
                break
            else:
                ops += nums[i]
                slack -= nums[i]
        return ops
        