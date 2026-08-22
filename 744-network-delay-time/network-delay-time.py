import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q=[]
       
        adj = [[] for _ in range(n+1)]
        for i in range(len(times)):
            src=times[i][0]
            dest=times[i][1]
            wt=times[i][2]
            adj[src].append((dest,wt))
            
        res=[float('inf')] * (n+1)
        res[k]=0
        heapq.heappush(q,(0,k))
        while q:
            wet,source=heapq.heappop(q)
            if wet > res[source]:
                continue
            for i in range(len(adj[source])):
                neigh=adj[source][i][0]
                newwt=adj[source][i][1]
                if res[neigh] > wet + newwt:
                    res[neigh]= wet + newwt
                    
                    heapq.heappush(q,(res[neigh],neigh))
        ans= max(res[1:])
        if ans== float('inf'):
            return -1
        return ans
