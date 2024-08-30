from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
     
        return res


        # n = len(cost)
        # def backtrack(startStation,currStation,gasremaining,stationsVisited):

        #     if stationsVisited == n:
        #         return True
            
        #     nextStation = (currStation + 1)%n
        #     gasremaining += gas[currStation] - cost[currStation]

        #     if gasremaining < 0:
        #         return False

        #     return backtrack(startStation,nextStation,gasremaining,stationsVisited+1)

    
        # for i in range(n):
        #     if backtrack(i,i,0,0):
        #         return i
        # return -1



newObject = Solution()
print(newObject.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))