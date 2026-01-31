class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for source, dest, weight in edges:
            graph[source].append((dest, weight))
            graph[dest].append((source, 2*weight))
        dist = [math.inf]*n
        visited = [False]*n
        dist[0] = 0
        q = [(0, 0)]

        while q:
            curr, node = heapq.heappop(q)
            if node == n-1:
                return curr
            if visited[node]:
                continue
            visited[node] = True
            for neighbor, ncost in graph[node]:
                new_cost = curr + ncost
                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    heapq.heappush(q, (new_cost, neighbor))

        return -1
        