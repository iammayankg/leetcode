class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        curr = 0
        score = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[curr]:
                score += nums[curr] * (i - curr)
                curr = i
        
        if curr != len(nums) - 1:
            score += nums[curr] * (len(nums)-1 - curr)
        return score

        