class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        N = len(target)
        ops = target[0]
        for i in range(1, N):
            if target[i] > target[i-1]:
                ops += target[i] - target[i-1]
        return ops


        