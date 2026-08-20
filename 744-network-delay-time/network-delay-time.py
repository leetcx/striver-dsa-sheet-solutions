import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[]for _ in range(n+1)]
        for i in range(len(times)):
            sr=times[i][0]
            dest=times[i][1]
            weight=times[i][2]
            adj[sr].append((dest,weight))
            
        pq=[]
        distance=[float('inf')] * (n+1)
        distance[k]=0
        heapq.heappush(pq,(0,k))
        while pq:
            dist,node=heapq.heappop(pq)
            if dist> distance[node]:
                continue
            for i in range(len(adj[node])):
                neigh=adj[node][i][0]
                wt=adj[node][i][1]
                if dist+wt < distance[neigh]:
                    distance[neigh]=dist+wt
                    heapq.heappush(pq,(dist+wt,neigh))
        ans=max(distance[1:]) 
        return ans if ans != float('inf') else -1