class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev_zero = -1
        for idx, num in enumerate(nums):
            if num == 0 and prev_zero == -1:
                prev_zero = idx
            elif num != 0 and prev_zero != -1:
                nums[prev_zero] = num
                nums[idx] = 0
                prev_zero += 1
        