from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegree=[0]*numCourses
        adj=[[] for _ in range(numCourses)]

        for i,j in prerequisites:
            adj[i].append(j)
            indegree[j]+=1

        st=[]
        for i in range(numCourses):
            if indegree[i]==0:
                st.append(i)

        ans=[[] for _ in range(numCourses)]
        while st:
            x=st.pop(0)
            for i in adj[x]:
                for j in ans[x]:
                    if j not in ans[i]:
                        ans[i].append(j)
                ans[i].append(x)
                indegree[i]-=1
                if indegree[i]==0:
                    st.append(i)
        lst=[]
        for i,j in queries:
            if i in ans[j]:
                lst.append(True)
            else:
                lst.append(False)
        return lst