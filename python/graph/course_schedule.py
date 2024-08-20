from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {i:[] for i in range(numCourses)} 

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        inDegree = [0] * numCourses

        for i in range(numCourses):
            for nei in adjList[i]:
                inDegree[nei] += 1
        queue = deque()
        for j in range(numCourses):
            if inDegree[j] == 0:
                queue.append(j)
        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)
        
            for it in adjList[node]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    queue.append(it)
        if len(topo) == numCourses:
            return True 
        return False

newObject = Solution()
print(newObject.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))

