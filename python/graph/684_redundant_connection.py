from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        noOfEdges = len(edges) + 1
        parent = [i for i in range(noOfEdges)]
        rank = [0 for i in range(noOfEdges)]

        def findParent(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a,b):
            p1, p2  = findParent(a),findParent(b)
            
            if p1 == p2:
                return False
            elif rank[p1] > rank[p2]:
                parent[p2] = p1 
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        

        for a,b in  edges:
            if not union(a,b):
                return [a,b]

        return (parent,rank)

newObject = Solution()

print(newObject.findRedundantConnection([[1,2],[1,3],[2,3]]))