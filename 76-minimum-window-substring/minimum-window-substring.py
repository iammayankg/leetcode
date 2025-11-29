class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        countW = Counter()
        
        left = 0
        res = len(s) + 1
        ress = ""
        required = len(t)
        formed = 0
        for right in range(len(s)):
            ch = s[right]
            if ch not in countT:
                continue
            countW[ch] += 1
            while countW >= countT:
                chLeft = s[left]
                if right - left + 1 < res:
                    res = min(res, right-left + 1)
                    ress = s[left:right+1]
                if chLeft in countT:
                    countW[chLeft] -= 1
                left += 1
                
        return ress