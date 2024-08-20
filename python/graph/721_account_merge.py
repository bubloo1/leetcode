from typing import List
from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        newUnionFindObj = UnionFind(len(accounts))

        findEmailGroup = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in findEmailGroup:
                    newUnionFindObj.union(i, findEmailGroup[email])
                else:
                    findEmailGroup[email] = i
        
        groupEmails = defaultdict(list)
        for email,i in findEmailGroup.items():
            leader = newUnionFindObj.findParent(i)
            groupEmails[leader].append(email)
        
        res = []
        for i, email in groupEmails.items():
            name = accounts[i][0]
            res.append([name] + sorted(groupEmails[i]))
        return res


                     


newObject = Solution()

print(newObject.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                                        ["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],
                                        ["John","johnnybravo@mail.com"]]))