class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append((v,w))
        distance=[float('inf')] *n
        distance[src]=0
        for i in range(k+1):
            temp=distance.copy()
            for u,v,w in flights:
                if distance[u] != float('inf'):
                    if distance[u]+w<temp[v]:
                        temp[v]=distance[u]+w
            distance=temp
        if distance[dst]==float('inf'):
            return -1
        return distance[dst]