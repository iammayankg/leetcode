class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        N = len(word)
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]

        def isValid(x, y):
            return 0 <= x < ROWS and 0<=y<COLS

        def dfs(x, y, index, visited):
            if index == N:
                return True
            if board[x][y] != word[index]:
                return False
            if (x,y) in visited:
                return False
            visited.add((x,y))
            res = False
            for vector in directions:
                nx, ny = x + vector[0], y + vector[1]
                if isValid(nx, ny):
                    res |= dfs(nx, ny, index+1, visited)
                    if res:
                        return True
            
            visited.remove((x,y))
            return True if index + 1 == N else res


        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0, set()):
                    return True
        return False
        