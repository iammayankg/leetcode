class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        delCost = defaultdict(int)
        for idx, ch in enumerate(s):
            delCost[ch] += cost[idx]

        maxCost = 0
        totalCost = 0
        for ch, cost in delCost.items():
            maxCost = max(maxCost, cost)
            totalCost += cost
        return totalCost - maxCost