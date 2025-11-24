class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N1, N2 = len(str1), len(str2)
        if N1 < N2:
            str1, str2 = str2, str1
            N1, N2 = N2, N1
        res = ""
        for i in range(N2, 0, -1):
            if N1 % (i) == 0 and N2 % i == 0:
                factor = N1 // (i)
                factor2 = N2 // i
                curr = str2[:i]
                if curr * factor == str1 and curr *factor2 == str2:
                    return curr
        return res
        