class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, sum(nums)
        answer = 0
        for idx, num in enumerate(nums):
            if num == 0:
                if 0 <= right-left <= 1:
                    answer += 1
                if 0 <= left - right <= 1:
                    answer += 1
            else:
                left += num
                right -= num

        return answer