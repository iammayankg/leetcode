class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0]* (COLS+1) for _ in range(ROWS+1)]
        for i in range(ROWS):
            prefix = 0
            for j in range(COLS):
                prefix += matrix[i][j]
                r, c = i + 1, j + 1
                self.sumMat[r][c] = self.sumMat[r-1][c] + prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.sumMat[r2][c2]
        top = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1-1]
        topLeft = self.sumMat[r1-1][c1-1]
        return bottomRight - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)