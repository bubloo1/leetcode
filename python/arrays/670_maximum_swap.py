class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        maxDigit = "0"
        maxI= -1
        swapI = swapJ = -1

        for i in reversed(range(len(num))):
            #max
            if num[i] > maxDigit:
                maxDigit = num[i]
                maxI = i
            
            #swap
            if num[i] < maxDigit:
                swapI,swapJ = i, maxI
        num[swapI],num[swapJ] = num[swapJ],num[swapI]
        
        return int("".join(num))
        


newObject = Solution()
print(newObject.maximumSwap(736))