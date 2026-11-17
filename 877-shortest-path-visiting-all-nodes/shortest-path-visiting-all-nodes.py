from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        q=deque()
        
        n=len(graph)
        mainmask=(1<<n)-1
        visited={}
        for i in range(n):
            maskvalue= 1<<i
            q.append((i,maskvalue))
            visited[(i,maskvalue)]=1
        path=0
        while q:
            n=len(q)
            path+=1
            while n:
                node,mask=q.popleft()
                for neigh in graph[node]:
                    newmask=mask | (1<<neigh)
                    if newmask==mainmask:
                        return path
                    if (neigh,newmask) not in visited:
                        visited[(neigh,newmask)]=1
                        q.append((neigh,newmask))
                n-=1
        return 0
        
