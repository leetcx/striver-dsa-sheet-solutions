import heapq
class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.adj=[[] for _ in range(n)]
        for u,v,cost in edges:
            self.adj[u].append((v,cost))
            

        

    def addEdge(self, edge: list[int]) -> None:
        u,v,cost=edge
        self.adj[u].append((v,cost))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        n=len(self.adj)
        self.minheap=[]
        heapq.heappush(self.minheap,(0,node1))
        self.distance=[float('inf')] * n
        self.distance[node1]=0
        while self.minheap:
            dist,node=heapq.heappop(self.minheap)
            if dist>self.distance[node]:
                continue
            for neigh in self.adj[node]:
                nody=neigh[0]
                w=neigh[1]
                if dist+w<self.distance[nody]:
                    self.distance[nody]=dist+w
                    heapq.heappush(self.minheap,(dist+w,nody))
        return self.distance[node2] if self.distance[node2] != float('inf') else -1
                

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)