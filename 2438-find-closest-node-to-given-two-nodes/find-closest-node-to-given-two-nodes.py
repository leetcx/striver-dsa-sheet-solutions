from collections import deque
class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n=len(edges)
        adj = [[] for _ in range(n)]

        for u in range(n):
            v = edges[u]
            if v != -1:
                adj[u].append(v)   
        node1dist=[float('inf')] * n
        visited=[False] * n
        visited[node1]=True
        node1dist[node1]=0
        minheap=[]
        minheap.append((0,node1))
        while minheap:
            dist,node=heapq.heappop(minheap)
            if dist>node1dist[node]:
                continue
            for neigh in adj[node]:
                if node1dist[neigh]>1+dist:
                    node1dist[neigh]=1+dist
                
                    minheap.append((1+dist,neigh))
        node2dist=[float('inf')] * n
       
        node2dist[node2]=0
        minheap=[]
        heapq.heappush(minheap,(0,node2))
        while minheap:
            dist,node=heapq.heappop(minheap)
            if dist>node2dist[node]:
                continue
            for neigh in adj[node]:
                if node2dist[neigh]>1+dist:
                    node2dist[neigh]=1+dist
                
                    heapq.heappush(minheap,(1+dist,neigh))
        z=len(node1dist)
        p=[]
        ans=float('inf')
        result=-1
        for i in range(z):
            if node1dist[i]!= float('inf') and node2dist[i]!=float('inf'):
                s=max(node1dist[i],node2dist[i])
                if s<ans:
                    ans=s
                    result=i
        return result


        
