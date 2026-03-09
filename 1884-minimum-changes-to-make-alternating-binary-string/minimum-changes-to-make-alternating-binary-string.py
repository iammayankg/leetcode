class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        start0 = 0
        for i in range(n):
            if i % 2 == 0:
                if s[i] == "1":
                    start0 += 1
            else:
                if s[i] == "0":
                    start0 += 1
        return min(start0, n-start0)
