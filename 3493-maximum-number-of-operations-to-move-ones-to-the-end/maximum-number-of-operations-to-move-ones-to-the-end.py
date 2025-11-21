class Solution:
    def maxOperations(self, s: str) -> int:
        cnt_one = 0
        ops = 0
        idx = 0
        while idx < len(s):
            num = s[idx]
            if num == '1':
                cnt_one += 1
                idx += 1
            else:
                while idx < len(s) and s[idx] == '0':
                    idx += 1
                ops += cnt_one
        return ops
        
        