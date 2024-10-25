from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
        for k in range(n):
            start = 0
            end = len(matrix) - 1
            while start < end:
                matrix[k][start],matrix[k][end] = matrix[k][end], matrix[k][start]
                start += 1
                end -= 1

        # n  = len(matrix) - 1
        # dummyMatrix = [[0 for i in range(len(matrix))] for j in range(len(matrix))]

       
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)-1,-1,-1):
        #         dummyMatrix[i][n - j] = matrix[j][i]
        # matrix = dummyMatrix




