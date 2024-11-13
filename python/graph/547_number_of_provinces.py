from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
    
    def findParent(self,p):
        p = self.parent[p]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self,a,b):
        a,b = self.findParent(a), self.findParent(b)

        if a == b:
            return False
        elif self.rank[a] > self.rank[b]:
            self.parent[b] = a
            self.rank[a] += self.rank[b]
        else:
            self.parent[a] = b
            self.rank[b] += self.rank[a]
        
        return True



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        unionfindObj = UnionFind(n)

        for i in range(n):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    unionfindObj.union(i,j)

        print(unionfindObj.parent,"parent")
        print(3//2,"parent")
        return len(set(unionfindObj.findParent(i) for i in range(n)))
        

        # one way of doing this is dfs
        # adjList = defaultdict(list)
        # visited = set() 
        # provinces = 0

        # def dfs(i):
        #     visited.add(i)
        #     for nei in adjList[i]:
        #         if nei not in visited:
        #             dfs(nei)

        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected[0])):
        #         if isConnected[i][j] == 1:
        #             adjList[i].append(j)
        
        # for i in range(len(isConnected)):
        #     if i not in visited:
        #         provinces += 1
        #         dfs(i)
        # return provinces
    
newObject =Solution()
print(newObject.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))