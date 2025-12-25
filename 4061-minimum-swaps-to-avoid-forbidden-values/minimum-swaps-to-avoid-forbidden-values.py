class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        numCount = Counter(nums)
        forbCount = Counter(forbidden)
        N = len(nums)

        for num, count in numCount.items():
            if forbCount[num] > N - count:
                return -1

        conflicts = 0
        badCounts = Counter()
        maxFreq = 0

        for i in range(N):
            if nums[i] == forbidden[i]:
                conflicts += 1
                badCounts[nums[i]] += 1
                maxFreq = max(maxFreq, badCounts[nums[i]])

        if conflicts == 0:
            return 0

        pairs = min(conflicts//2, conflicts - maxFreq)
        return conflicts -pairs
        