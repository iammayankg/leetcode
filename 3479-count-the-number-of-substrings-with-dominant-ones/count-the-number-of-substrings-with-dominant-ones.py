class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        nextZero = [N] * N
        for i in range(N-2, -1, -1):
            if s[i+1]=="0":
                nextZero[i] = i + 1
            else:
                nextZero[i] = nextZero[i+1]

        result = 0
        for i in range(N):
            zeros = 1 if s[i] == "0" else 0
            r = i
            while zeros*zeros < N:
                j = nextZero[r]
                ones = j-i - zeros
                if ones >= zeros*zeros:
                    result += min(j-r, ones-zeros*zeros + 1)
                zeros += 1
                if j == N:
                    break
                r = j
                # j = nextZero[j]
        return result
        