class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        component_count = [0]

        def dfs(node, parent):
            sum = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    sum += dfs(neighbor, node)

                sum = sum %k

            sum += values[node]
            sum = sum %k
            if sum == 0:
                component_count[0] += 1

            return sum

        dfs(0, -1)
        return component_count[0]
        