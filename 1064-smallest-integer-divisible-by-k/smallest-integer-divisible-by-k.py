class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        N = 1
        remainder = 1
        ans = 1
        seen = set()
        while remainder%k != 0:
            N = remainder * 10 + 1
            remainder = N %k
            ans += 1

            if remainder in seen:
                return -1
            else:
                seen.add(remainder)
            
        return ans
        