from collections import deque
class Solution:
    def findOrder(self, n: int, pr: List[List[int]]) -> List[int]:
        res=[]
        adj=[[] for _ in range(n)] 
        indegree=[0] * n
        q=deque()
        for i in range(len(pr)):
            s=pr[i][0]
            d=pr[i][1]
            adj[d].append(s)
            indegree[s]+=1
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        while q:
            p=len(q)
            for i in range(p):
                node=q.popleft()
                res.append(node)
                for i in range(len(adj[node])):
                    neigh=adj[node][i]
                    indegree[neigh]-=1
                    if indegree[neigh]==0:
                        q.append(neigh)
        if len(res) !=n:
            return []        
        return res