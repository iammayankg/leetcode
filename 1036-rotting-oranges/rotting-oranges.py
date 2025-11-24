class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dirs = [(0,1), (1,0), (0,-1), (-1, 0)]
        def isValid(x, y):
            return 0<=x<ROWS and 0<=y<COLS

        EMPTY, FRESH, ROTTEN = 0, 1, 2
        q = deque()
        fresh_count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == ROTTEN:
                    q.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh_count += 1
        
        minutes = 0
        while q and fresh_count:
            N = len(q)
            minutes += 1
            for _ in range(N):
                x, y = q.popleft()
                for vector in dirs:
                    nx, ny = x + vector[0], y + vector[1]
                    if isValid(nx, ny) and grid[nx][ny] == FRESH:
                        grid[nx][ny] = ROTTEN
                        q.append((nx, ny))
                        fresh_count -= 1
            if fresh_count == 0:
                break
        return minutes if fresh_count == 0 else -1


        