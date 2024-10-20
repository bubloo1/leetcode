from typing import List
from collections import defaultdict,deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)
      
        for flight in flights:
            adj[flight[0]].append((flight[1],flight[2]))

        queue = deque([(0,(src,0))])

        dist = [float("inf")] * n
        dist[src] = 0

        while queue:
            stops, (node,cost) = queue.popleft()

            if stops > k:
                continue

            for adjNode, newCost in adj[node]:

                if  newCost + cost < dist[adjNode] and stops <= k:
                    dist[adjNode] = (newCost + cost)
                    queue.append((stops + 1, (adjNode, cost + newCost)))

        
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]


