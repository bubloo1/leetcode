class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = {i:[] for i in range(n)}
        print(adjList)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(curr , par):
            time = 0
            for child in adjList[curr]:
                if child == par:
                    continue
                childTime = dfs(child, curr)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time
        return dfs(0, -1)

