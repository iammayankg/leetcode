class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = defaultdict(lambda: 0)
        ROWS, COLS = len(grid), len(grid[0])
        dp[(0, 0, grid[0][0]%k)] = 1
        MOD = 10**9 + 7

        def isValid(x, y):
            return 0 <= x < ROWS and 0 <= y < COLS

        for x in range(ROWS):
            for y in range(COLS):
                nx, ny = x + 1, y
                if isValid(nx, ny):
                     for m in range(k):
                        prev = dp[(x, y, m)]
                        curr = (m+grid[nx][ny])%k
                        dp[(nx, ny, curr)] += prev
                nx, ny = x, y + 1
                if isValid(nx, ny):
                     for m in range(k):
                        prev = dp[(x, y, m)]
                        curr = (m+grid[nx][ny])%k
                        dp[(nx, ny, curr)] += prev

        return dp[(ROWS-1, COLS-1, 0)] % MOD