class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = self.parent[px]
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = self.parent[py]
        else:
            self.parent[py] = self.parent[px]
            self.rank[px] += 1

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        uf = UnionFind(row*col + 2)
        grid = [[1] * col for _ in range(row)]
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]

        for i in range(len(cells)-1,-1,-1):
            r,c = cells[i][0]-1, cells[i][1]-1
            grid[r][c] = 0
            curr = r * col + c + 1
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    nxt = nr*col + nc + 1
                    uf.union(curr, nxt)

            if r == 0:
                uf.union(0, curr)
            if r == row-1:
                uf.union(row*col + 1, curr)
            if uf.find(0) == uf.find(row*col + 1):
                return i

        