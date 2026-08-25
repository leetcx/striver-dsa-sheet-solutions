import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for i in range(len(times)):
            s=times[i][0]
            d=times[i][1]
            wt=times[i][2]
            adj[s].append((d,wt))
        res=[(float('inf'))] * (n+1)

   
        q=[]
        heapq.heappush(q,(0,k))
        res[k]=0
        while q:
            dist,node=heapq.heappop(q)
            if dist > res[node]:
                continue
            for i in range(len(adj[node])):
                neigh=adj[node][i][0]
                new=adj[node][i][1]
                if   res[neigh] > new + dist:
                    res[neigh]=new+dist
                    heapq.heappush(q,(res[neigh],neigh))
        p=max(res[1:])
        if p != (float('inf')):
            return p
        return -1
                
