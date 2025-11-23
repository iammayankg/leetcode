class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            count = Counter(nums[i:i+k])
            if len(count) <= x:
                res.append(sum(nums[i:i+k]))
            else:
                pairs = list(count.items())
                pairs.sort(key=lambda p: (p[1], p[0]), reverse=True)
                res.append(sum([c*v for v,c in pairs[:x]]))
        return res
        