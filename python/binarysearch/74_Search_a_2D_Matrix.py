class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # i = 0
        # while target > matrix[i][-1] and i < len(matrix) - 1:
        #     i += 1

        # l = 0
        # r = len(matrix[0]) - 1
        # while l <= r:
        #     m = (l + r)//2
        #     if(matrix[i][m] > target):
        #         r = m - 1
        #     elif(matrix[i][m] < target):
        #         l = m +1
        #     else:
        #         return True
        # return False

  

        # ROWS, COLS = len(matrix), len(matrix[0])

        # top, bot = 0, ROWS - 1
        # while top <= bot:
        #     row = (top + bot) // 2
        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bot = row - 1
        #     else:
        #         break

        # if not (top <= bot):
        #     return False
        # row = (top + bot) // 2
        # l, r = 0, COLS - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if target > matrix[row][m]:
        #         l = m + 1
        #     elif target < matrix[row][m]:
        #         r = m - 1
        #     else:
        #         return True
        # return False
        # lo = 0
        # if not matrix:
        #     return False
        # hi = (len(matrix) * len(matrix[0])) - 1


        # while lo <= hi:
        #     mid = (lo + (hi - lo) // 2)
        #     if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
        #         return True
        #     if matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
        #         lo = mid + 1
        #     else:
        #         hi = mid - 1
        # return False

        i = 0
        j = len(matrix[0]) - 1
        # if ((len(matrix) - 1) == 0) and j == 0 and matrix[i][j] == target:
        #     return True
       
        while j >= 0 and i <= len(matrix) - 1:
            if matrix[i][j] == target:
                return True    
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
            