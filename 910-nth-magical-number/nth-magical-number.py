class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        g = math.gcd(a, b)
        lcm = (a*b)//g
        low = min(a, b)
        high = low * n
        MOD = 10**9 + 7

        while low < high:
            mid = (low + high)//2
            cnt = mid//a + mid//b - mid//lcm
            if cnt < n:
                low = mid + 1
            else:
                high = mid
        return high%MOD
        