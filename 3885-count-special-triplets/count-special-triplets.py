class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        counts = Counter(nums)
        MOD = 10**9 + 7
        cnt = 0
        currCount = defaultdict(int)
        for idx, num in enumerate(nums):
            counts[num] -= 1
            leftCount = currCount[num*2]
            rightCount = counts[num*2]
            cnt += leftCount*rightCount
            cnt %= MOD
            currCount[num] += 1
        return cnt