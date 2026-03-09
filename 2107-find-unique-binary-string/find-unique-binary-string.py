class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        seen = set()
        for num in nums:
            seen.add(int(num, 2))
        maxval = 2**n -1
        for i in range(0, maxval+1):
            if i not in seen:
                return f"{i:0{n}b}"
        