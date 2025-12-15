class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0]*n
        self.disjoint = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.disjoint -= 1
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for source, target in edges:
            uf.union(source, target)
        component = Counter()
        for i in range(n):
            component[uf.find(i)] += 1
        result = 0
        x = n
        for cid, csize in component.items():
            result += csize * (x-csize)
            x = x-csize
        return result


        