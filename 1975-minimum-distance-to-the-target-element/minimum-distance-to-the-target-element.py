class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        retVal = len(nums) + 1
        for idx, num in enumerate(nums):
            if num == target:
                retVal = min(retVal, abs(idx-start))
        return retVal
        