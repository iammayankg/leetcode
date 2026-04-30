class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxSoFar = 0

        for num in numset:
            if num - 1 not in numset:
                curr = 1
                temp = num + 1
                while temp in numset:
                    curr += 1
                    temp += 1
                maxSoFar = max(maxSoFar, curr)
        return maxSoFar
            