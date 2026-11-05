from collections import deque
class Solution:
    def findOrder(self, n: int, pr: list[list[int]]) -> list[int]:
        indeg=[0] * n
        q=deque()
        for i in range(len(pr)):
            indeg[pr[i][0]]+=1
        adj=[[] for _ in range(n)]
        for u,v in pr:
            adj[v].append(u)
        for p in range(len(indeg)):
            if indeg[p]==0:
                q.append(p)
        ans=[]
        for z in range(len(adj)):
            while q:
                node=q.popleft()
                ans.append(node)
                for neigh in adj[node]:
                    indeg[neigh]-=1
                    if indeg[neigh]==0:
                        q.append(neigh)
        if len(ans)==n:
            return ans
        return []
        

        
