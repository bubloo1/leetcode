#Given a sorted dictionary of an alien language having N words and k starting alphabets of 
#standard dictionary. Find the order of characters in the alien language. If no valid ordering of letters is possible, then return "".
#Note: Many orders may be possible for a particular test case, thus you may 
#return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.

from collections import deque, defaultdict

class Solution:
    # works for multiple components
    
    def topoSort(self, V, adj):
        indegree = [0] * V
        
        # Calculate the indegree of each node
        for i in range(V):
            for neighbor in adj[i]:
                indegree[neighbor] += 1

        # Queue for nodes with 0 indegree
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        # Process the nodes
        while q:
            node = q.popleft()
            topo.append(node)
            
            # Decrease the indegree of neighboring nodes
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return topo

    def findOrder(self, dict, N, K):
        adj = defaultdict(list)
        
        # Build the adjacency list
        for i in range(N - 1):
            s1 = dict[i]
            s2 = dict[i + 1]
            length = min(len(s1), len(s2))
            
            # Find the first differing character and create the directed edge
            for j in range(length):
                if s1[j] != s2[j]:
                    adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                    break

        topo = self.topoSort(K, adj)

        # Convert topological order to characters
        ans = ''.join([chr(i + ord('a')) for i in topo])
        return ans


if __name__ == "__main__":
    N = 5
    K = 4
    dict = ["baa", "abcd", "abca", "cab", "cad"]
    obj = Solution()
    ans = obj.findOrder(dict, N, K)
    
    for ch in ans:
        print(ch, end=' ')
    print()
