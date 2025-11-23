class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 + 1

        res = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x:
            if res > INT_MAX/10:
                return 0

            curr = x % 10
            if INT_MAX - curr < res:
                return 0
            res = res * 10 + curr
            x = x//10
        return res * sign
        