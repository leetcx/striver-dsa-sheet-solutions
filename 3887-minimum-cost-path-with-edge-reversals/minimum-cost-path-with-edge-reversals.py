import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
               
            adj[u].append((v,w))  
            adj[v].append((u,2*w))
        minheap=[]
        distance=[float('inf')] * n
        distance[0]=0
        heapq.heappush(minheap,(0,0)) 
        while minheap:
            dist,node=heapq.heappop(minheap)
            if dist>distance[node]:
                continue
            if node==n-1:
                return dist
            for neigh in adj[node]:
                nody=neigh[0]
                disi=neigh[1]
                if distance[nody] >dist+disi:
                    distance[nody]=dist+disi
                    heapq.heappush(minheap,(dist+disi,nody))
        return -1
        