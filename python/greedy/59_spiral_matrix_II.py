from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        res = [[0] * n for i in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        num = 1
        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res[top][i] = num
                num += 1
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res[i][right - 1] = num
                num += 1
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res[bottom - 1][i] = num
                num += 1
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res

newObject = Solution()
print(newObject.generateMatrix(3))