import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
       
        
       
        dist = [[float('inf')] * 26 for _ in range(26)]
        n=len(cost)
        for i in range(26):
            dist[i][i] = 0
        for j in range(n):
            u=ord(original[j])-ord('a')
            v=ord(changed[j])-ord('a')
            wt=cost[j]
            dist[u][v]=min(dist[u][v],wt)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        cost=0
        for i in range(len(source)):
            src=ord(source[i])-ord('a')
            dest=ord(target[i])-ord('a')
            if dist[src][dest]==float('inf'):
                return -1
            cost+=dist[src][dest]
        return cost
        
        
