
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        components = 0
        
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        for i in range(n):
            if not visited[i]:
                components += 1
                visited[i] = True
                dfs(i)
    
        return components
    
newObject = Solution()
print(newObject.countComponents(6,[[0,1], [0,2]]))