from typing import List
from collections import defaultdict,deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Create adjacency list and sort destinations in lexical order
        graph = defaultdict(deque)
        for u, v in sorted(tickets):
            graph[u].append(v)
        
        result = []
        
        # Step 2: Perform DFS
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].popleft()  # Get the smallest lexical airport
                dfs(next_airport)
            result.append(airport)
        
        # Step 3: Start DFS from 'JFK'
        dfs('JFK')
        
        # Step 4: Reverse the result to get the itinerary
        return result[::-1]