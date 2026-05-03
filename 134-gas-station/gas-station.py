class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        total, curr = 0, 0
        start = 0
        for i in range(N):
            diff = gas[i]-cost[i]
            total += diff
            curr += diff
            if curr < 0:
                curr = 0
                start = i+1
        return start if total >=0 else -1

        