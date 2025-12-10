class Solution:
    def countTriples(self, n: int) -> int:
        def isSquare(c):
            lo, hi = 1, c
            while lo <= hi:
                mid  = (lo + hi)//2
                if mid*mid == c:
                    return mid
                elif mid*mid < c:
                    lo = mid+1
                else:
                    hi = mid - 1
            return -1
        cnt = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                s = isSquare(i**2 + j**2)
                if s != -1 and s <= n:
                    cnt += 1
        return cnt
        