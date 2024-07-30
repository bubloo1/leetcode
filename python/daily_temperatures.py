class Solution:
    def dailyTemperatures(self, temperatures):
        lenOfTempArray = len(temperatures)
        res = [0] * lenOfTempArray
        stack = []

        for i,t in enumerate(temperatures):

            while stack and stack[-1][0] < t:
                temp,index = stack.pop()
                res[index] = i - index
            stack.append((t,i))
        
        return res

# time complexity Olog(n)


newObject = Solution()

print(newObject.dailyTemperatures([73,74,75,71,69,72,76,73]))