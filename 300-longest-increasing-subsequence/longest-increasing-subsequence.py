import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curr = []

        for num in nums:
            idx = bisect.bisect_left(curr, num)
            if idx == len(curr):
                curr.append(num)
            else:
                curr[idx] = num
        return len(curr)