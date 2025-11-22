class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for num in nums:
            mod = num % 3
            if mod == 0:
                continue
            else:
                ops += 1
        return ops
        