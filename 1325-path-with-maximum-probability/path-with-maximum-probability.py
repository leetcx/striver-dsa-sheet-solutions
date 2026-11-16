import heapq
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
      
        minheap=[]
        adj=[[] for _ in range(n)]
        for i in range(len(edges)):
            u=edges[i][0]
            v=edges[i][1]
            wt=succProb[i]
            adj[u].append((v,wt))
            adj[v].append((u,wt))
        heapq.heappush(minheap,(-1.0,start_node))
        distance=[0.0] * n
        distance[start_node]=1.0
        while minheap:
            prob,node=heapq.heappop(minheap)
            probability=-prob
            if probability<distance[node]:
                continue
            for neigh in adj[node]:
                nody=neigh[0]
                w=(neigh[1])
                new_prob = distance[node] * w
                if new_prob>distance[nody]:
                    distance[nody]=new_prob
                    heapq.heappush(minheap,(-new_prob,nody))
        return distance[end_node]
            
            

