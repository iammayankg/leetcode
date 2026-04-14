import math
from functools import cache
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        factoryPos = []
        for f, c in factory:
            factoryPos.extend([f]*c)

        memo = [[None] * (len(factoryPos)+1) for _ in range(len(robot))]
        
        def dp(roboId, factoryId):
            if roboId == len(robot):
                return 0
            if factoryId == len(factoryPos):
                return math.inf
            if memo[roboId][factoryId] is not None:
                return memo[roboId][factoryId]
            take = abs(robot[roboId] - factoryPos[factoryId]) + dp(roboId+1, factoryId+1)
            skip = dp(roboId, factoryId + 1)
            val = min(take, skip)
            memo[roboId][factoryId] = val
            return val
        return dp(0, 0)
        