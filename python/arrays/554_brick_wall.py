from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0 : 0}

        for brickRow in wall:
            total = 0
            for brick in brickRow[:-1]:
                total += brick 
                countGap[total] = 1 + countGap.get(total, 0)
        
        return len(wall) - max(countGap.values())
    

newObject = Solution()
print(newObject.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))