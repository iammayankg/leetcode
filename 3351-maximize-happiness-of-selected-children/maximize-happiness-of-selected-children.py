class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        N = len(happiness)
        # happiness = happiness[::-1]
        total = 0
        i = 0
        for i in range(k):
            total += max(happiness[i] - i,0)
        return total