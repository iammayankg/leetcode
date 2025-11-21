class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sC = collections.Counter(s)
        sT = collections.Counter(t)

        for char, count in sT.items():
            if sC[char] == 0:
                return char
            elif sT[char] > sC[char]:
                return char
        return t[0]
        