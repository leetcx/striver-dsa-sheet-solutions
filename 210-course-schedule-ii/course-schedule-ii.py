from collections import deque
class Solution:
    def findOrder(self, n: int, pr: List[List[int]]) -> List[int]:
        indegree=[0] * n
        adj=[[] for _ in range(n)]
        q=deque()
        res=[]

        for i in range(len(pr)):
            s=pr[i][0]
            d=pr[i][1]
            adj[d].append(s)
            indegree[s]+=1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node=q.popleft()
            res.append(node)
            for i in range(len(adj[node])):
                neigh=adj[node][i]
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if len(res) != n:
            return []
        return res

        


