class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        bosses = defaultdict(list)
        for u,v in hierarchy:
            bosses[u-1].append(v-1)

        def dfs(node):
            cost = present[node]
            dCost = cost//2

            dp0 = [0]*(budget+1)
            dp1 = [0]*(budget+1)

            subProfit0 = [0]*(budget+1)
            subProfit1 = [0]*(budget+1)

            usize = cost

            for child in bosses[node]:
                childDp0, childDp1, vsize = dfs(child)
                usize += vsize
                for i in range(budget, -1, -1):
                    for sub in range(min(vsize,i) + 1):
                        subProfit0[i] = max(subProfit0[i], subProfit0[i-sub] + childDp0[sub])
                        subProfit1[i] = max(subProfit1[i], subProfit1[i-sub] + childDp1[sub])

            for i in range(budget+1):
                dp0[i] = subProfit0[i]
                dp1[i] = subProfit0[i]

                if i>=dCost:
                    dp1[i] = max(subProfit0[i], subProfit1[i-dCost] + future[node] - dCost)

                if i >= cost:
                    dp0[i] = max(subProfit0[i], subProfit1[i-cost] + future[node] - cost)

            return dp0, dp1, usize

        return dfs(0)[0][budget]
        