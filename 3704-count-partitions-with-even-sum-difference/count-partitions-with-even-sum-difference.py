class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        N = len(nums)
        leftSum = [0] * N
        rightSum = [0] * N

        currSum = 0
        for i in range(1, N):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        for i in range(N-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
        cnt = 0
        for i in range(1,N):
            if abs(leftSum[i] - rightSum[i] - nums[i])%2 == 0:
                cnt += 1
        return cnt
        