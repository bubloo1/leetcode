from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]):
        n = len(matrix)

        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        print(matrix,"matrix")
        for k in range(n):
            start = 0
            end = n - 1
            while start < end:
                matrix[k][start],matrix[k][end] = matrix[k][end], matrix[k][start]
                start += 1
                end -= 1
                
        return matrix



newObject = Solution()
print(newObject.rotate([[1,2,3],[4,5,6],[7,8,9]]))