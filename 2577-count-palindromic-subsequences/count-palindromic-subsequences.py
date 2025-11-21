class Solution:
    def countPalindromes(self, s: str) -> int:
        N = len(s)
        one_prefix = [0] * 10
        two_prefix = [[0] * 10 for i in range(10)]

        one_suffix = [0] * 10
        two_suffix = [[0] * 10 for i in range(10)]

        MODULO = 10**9 + 7

        for ch in reversed(s):
            x = int(ch)
            for i in range(10):
                two_suffix[x][i] += one_suffix[i]
            one_suffix[x] += 1
        cnt = 0
        for idx, ch in enumerate(s):
            x = int(ch)
            one_suffix[x] -= 1
            for i in range(10):
                two_suffix[x][i] -= one_suffix[i]
            
            for i in range(10):
                for j in range(10):
                    cnt += (two_prefix[i][j] * two_suffix[j][i]) % MODULO
                    cnt = cnt % MODULO

            for i in range(10):
                two_prefix[i][x] += one_prefix[i]
            one_prefix[x] += 1

        return cnt
            

        