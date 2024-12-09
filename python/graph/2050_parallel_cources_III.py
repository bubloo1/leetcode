class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Adjacency list and in-degree array
        adj = defaultdict(list)
        indegree = [0] * n
        
        # Build the graph and in-degree array
        for u, v in relations:
            adj[u - 1].append(v - 1)  # Convert 1-based to 0-based indexing
            indegree[v - 1] += 1
        
        # Queue to store courses with no prerequisites
        queue = deque()
        max_time = [0] * n  # max_time[i] = max time to complete the i-th course
        
        # Initialize courses with no prerequisites
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                max_time[i] = time[i]
        
        # Topological sort
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                # Update the maximum time for course v
                max_time[v] = max(max_time[v], max_time[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        # Return the maximum time from all courses
        return max(max_time)