from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for crs,pre in prerequisites:
            adj[pre].append(crs)
    
        for i in range(numCourses):
            for it in adj[i]:
                indegree[it] += 1

        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            node = q.pop(0)
            topo.append(node)
            
            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        if len(topo) == numCourses:
            return topo
        return []
        