import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for i in range(len(times)):
            src=times[i][0]
            dest=times[i][1]
            we=times[i][2]
            adj[src].append((dest,we))
        q=[]
        visited=[False] *(n+1)
        res=[float('inf')] * (n+1)
        heapq.heappush(q,(0,k))
        res[k]=0
        while q:
            dist,node=heapq.heappop(q)
            if dist > res[node]:
                continue
            visited[node]=True
            for p in range(len(adj[node])):
                s=adj[node][p][0]
                wt=adj[node][p][1]
               
                if visited[s]==False and res[s] > dist+ wt:
                    res[s]= dist+wt
                    heapq.heappush(q,(res[s],s))
        g=max(res[1:])
        if g == float('inf'):
            return -1
        return g
        




































