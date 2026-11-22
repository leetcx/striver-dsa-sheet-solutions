from collections import deque

class Solution:
    def checkIfPrerequisite(self, n: int, pr: list[list[int]], queries: list[list[int]]) -> list[bool]:

        adj=[[] for _ in range(n)]
        indegree=[0]*n

        for u,v in pr:
            adj[u].append(v)
            indegree[v]+=1

        q=deque()

        for i in range(n):
            if indegree[i]==0:
                q.append(i)

        prerequisite=[set() for _ in range(n)]

        while q:
            node=q.popleft()

            for neigh in adj[node]:

                prerequisite[neigh].add(node)
                prerequisite[neigh].update(prerequisite[node])

                indegree[neigh]-=1

                if indegree[neigh]==0:
                    q.append(neigh)

        ans=[]

        for u,v in queries:
            ans.append(u in prerequisite[v])

        return ans