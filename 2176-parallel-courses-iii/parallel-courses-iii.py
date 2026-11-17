from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        adj=[[] for _ in range(n+1)]
        indeg=[0] *(n+1)
        for u,v in relations:
           
            adj[u].append(v)
            indeg[v]+=1
        q=deque()
        for i in range(1,len(indeg)):
            if indeg[i]==0:
                q.append(i)
        dp=[0] * (n+1)
        for i in range(len(time)):
            dp[i+1]=time[i]
        ans=0
        while q:
            n=len(q)
            temp=0
            while n:
                node=q.popleft()
                
                for neigh in adj[node]:
                    dp[neigh]=max(dp[neigh],dp[node]+time[neigh-1])
                    indeg[neigh]-=1
                    if indeg[neigh]==0:
                        q.append(neigh)
                n-=1
        return max(dp)