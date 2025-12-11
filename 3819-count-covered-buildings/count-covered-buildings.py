class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        dirX = defaultdict(list)
        dirY = defaultdict(list)

        for x, y in buildings:
            dirX[x].append(y)
            dirY[y].append(x)

        for x in dirX.keys():
            dirX[x].sort()
        for y in dirY.keys():
            dirY[y].sort()
        
        cnt = 0
        for x, y in buildings:
            above = 0 < bisect.bisect_left(dirY[y], x) < len(dirY[y])-1
            left = 0 < bisect.bisect_left(dirX[x], y) < len(dirX[x])-1
            
            if above and left:
                cnt += 1
        return cnt