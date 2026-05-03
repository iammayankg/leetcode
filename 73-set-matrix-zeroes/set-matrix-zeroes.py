class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isFirstColZero = False
        R, C = len(matrix), len(matrix[0])

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    if j == 0:
                        isFirstColZero = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        # print("one", matrix)
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # print("two", matrix)
        if matrix[0][0] == 0:
            for j in range(1, C):
                matrix[0][j] = 0

        # print("three", matrix)
        if isFirstColZero:
            for i in range(R):
                matrix[i][0] = 0
        

        