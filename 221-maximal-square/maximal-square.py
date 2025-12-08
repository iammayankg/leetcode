class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R,C = len(matrix), len(matrix[0])
        dp = [[0]*C for _ in range(R)]

        def isValid(x, y):
            return 0 <= x < R and 0 <= y < C

        dirs = [(0,-1), (-1, 0), (-1, -1)]
        ans = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == "1":
                    n = []
                    for d in dirs:
                        nx, ny  = i+d[0], j + d[1]
                        if isValid(nx, ny):
                            n.append((nx, ny))
                    
                    dp[i][j] = 1
                    if len(n) == 3:
                        dp[i][j] = min(dp[x][y] for x, y in n) + 1
                    ans = max(ans, dp[i][j])
        return ans*ans
                    
        