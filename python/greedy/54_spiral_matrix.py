from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # res = []
        # for i in range(len(matrix[0])-1):
        #     res.append(matrix[0][i])
        
        # for j in range(len(matrix)-1):
        #     res.append(matrix[j][len(matrix[0])-1])
        
        # for k in range(len(matrix[0])-1,-1,-1):
        #     res.append(matrix[len(matrix)-1][k])
        
        # for l in range(len(matrix[0])-1):
        #     res.append(matrix[len(matrix)-2][l])
        # return res

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res