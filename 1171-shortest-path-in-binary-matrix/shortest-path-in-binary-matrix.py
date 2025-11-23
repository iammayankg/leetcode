class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                directions.append((x, y))


        ROWS, COLS = len(grid), len(grid[0])
        distances = collections.defaultdict(lambda: math.inf)
        def isValid(x, y):
            return 0 <= x < ROWS and 0<= y < COLS

        minHeap = [(1, 0, 0)] if grid[0][0] == 0 else []
        if grid[0][0] == 0:
            distances[(0, 0)] = 1
        while minHeap:
            dist, x, y = heapq.heappop(minHeap)
            for vector in directions:
                nx, ny = x + vector[0], y + vector[1]
                if isValid(nx, ny) and grid[nx][ny] == 0 and distances[(nx, ny)] > dist + 1:
                    distances[(nx, ny)] = dist + 1
                    heapq.heappush(minHeap, (dist + 1, nx, ny))
        return distances[(ROWS-1, COLS-1)] if distances[(ROWS-1, COLS-1)] < math.inf else -1
