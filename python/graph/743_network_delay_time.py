from typing import List
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = {i:[] for i in range(1,n+1)}
        
        for u,v,w in times:
            adj_list[u].append((v,w))

        pq = [(0,k)]
        time = 0
        visited = set()
        while pq:

            currTime, currNode = heapq.heappop(pq)

            if currNode in visited:
                continue
            visited.add(currNode)
            time = currTime
            for nei,t in adj_list[currNode]:
                heapq.heappush(pq,(currTime + t,nei))

        return time if len(visited) == n else -1




newObject = Solution()
print(newObject.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))



