class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        numY = defaultdict(int)
        for p in points:
            numY[p[1]] += 1
        mod = 10**9 + 7
        total = 0
        currSum = 0

        for y in numY.values():
            n = (y * (y-1))//2
            currSum += total * n
            total += n
        return currSum%mod
        