from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if edges==[]:
            return [0]
        adj=[[] for _ in range(n)]
        degree=[0] * n
        for u,v in edges:
            adj[u].append(v)
            degree[v]+=1
            adj[v].append(u)
            degree[u]+=1
        q=deque()
        for i in range(len(degree)):
            if degree[i]==1:
                q.append(i)
        remaining=n
        while remaining>2:
            p=len(q)
            remaining-=p
            while p>0:
                node=q.popleft()
                for neigh in adj[node]:
                    degree[neigh]-=1
                    if degree[neigh]==1:
                        q.append(neigh)
                        
                p-=1
        return list(q)
