from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        intervals = sorted(zip(startTime,endTime,profit))
        dp = {}

        def findNextJob(index: int) -> int:
            low, high = index + 1, len(intervals) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if intervals[index][1] <= intervals[mid][0]:  
                    high = mid - 1  
                else:
                    low = mid + 1  
            return low  

        def dfs(index):
            if index == len(intervals):
                return 0

            if index in dp:
                return dp[index]

            # dont include
            res = dfs(index + 1)

            # include
            nextIndex = findNextJob(index)
            
            res = max(res,intervals[index][2] + dfs(nextIndex))
            dp[index] = res
            return res
        return dfs(0)


newObject = Solution()
print(newObject.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))


    