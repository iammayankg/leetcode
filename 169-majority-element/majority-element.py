class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_num, curr_count = nums[0], 1
        N = len(nums)
        for i in range(1, N):
            if curr_num == nums[i]:
                curr_count += 1
            else:
                curr_count -= 1
                if curr_count == 0:
                    curr_num = nums[i]
                    curr_count = 1
        return curr_num
        