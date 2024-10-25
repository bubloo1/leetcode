from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # columnArray = []
        # rowArray = []

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if(matrix[i][j] == 0):
        #             rowArray.append(i)
        #             columnArray.append(j)
        
        # for r in rowArray:
        #     for c in range(len(matrix[0])):
        #         matrix[r][c] = 0
        
        # for c in columnArray:
        #     for r in range(len(matrix)):
        #         matrix[r][c] = 0

        col_0 = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col_0 = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != 0:
                    # check for col & row:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if col_0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return matrix

