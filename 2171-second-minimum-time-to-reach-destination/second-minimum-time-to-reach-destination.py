class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], tam: int, change: int) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        mind1=[float('inf')]*(n+1)
        mind2=[float('inf')] *(n+1)
        minheap=[]
        heapq.heappush(minheap,(0,1))
        mind1[1]=0
        visited={}
        visited[1]=1
        while minheap:
            time,node=heapq.heappop(minheap)
                  
            if (time//change) %2==1:
                    time+=change-(time%change)
            time+=tam
            
            for neigh in adj[node]:
                
                if time<mind1[neigh]:
                    mind2[neigh]=mind1[neigh]
                    mind1[neigh]=time
                    heapq.heappush(minheap,(time,neigh))
                elif mind1[neigh]<time<mind2[neigh]:
                    mind2[neigh]=time
                    
                    heapq.heappush(minheap,(time,neigh))
        return mind2[n]

