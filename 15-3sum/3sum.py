class Solution:
    def twoSum(self, nums, result, curr):
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] == -curr:
                result.append([curr, nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif nums[i] + nums[j] < -curr:
                i += 1
            else:
                j -= 1


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()
        N = len(nums)
        for i in range(N):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(nums[i+1:], results, nums[i])
        return results
        