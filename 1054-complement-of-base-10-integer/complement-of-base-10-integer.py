class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        out = 0
        i = 0
        while n:
            x = 1 if n % 2 == 0 else 0
            out = out | (x << i)
            n = n >> 1
            i += 1
            # print(bin(n))
            # print(bin(out), '----')
        return out
        