class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0]*32

        def addNum(num):
            index = 0
            for index in range(32):
                if (num >> index) & 1:
                    bits[index] += 1
        
        for num in nums:
            addNum(num)

        res = 0
        for i in range(32):
            if bits[i] %3 != 0:
                res |= 1 << i
        return res if res < 1<<31 else res - (1<<32)        