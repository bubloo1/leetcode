from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # res = [] 

        # for i in range(len(arr)-1):
        #     if arr[i+1] > arr[i]:
        #         index = i + 1
        #         while index:
        #             res.append(arr[i+1])
        #             index -= 1
        # res.append(-1)
        # return res
        lenOfArr = len(arr)
        maxNum = arr[lenOfArr - 1]

        for i in range(lenOfArr-1,-1,-1):
            if i == lenOfArr -1:
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = maxNum
                maxNum = max(maxNum, temp)
        return arr