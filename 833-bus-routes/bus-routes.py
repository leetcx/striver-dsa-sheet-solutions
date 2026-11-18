from collections import deque
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        adj={}
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop not in adj:
                    adj[stop]=[]
                adj[stop].append(i)
        q=deque()
        visited={}
        if source not in adj or target not in adj:
            return -1
        for route in adj[source]:
            q.append(route)
            visited[route]=1
        level=0
        while q:
            n=len(q)
            level+=1
            while n>0:
                node=q.popleft()
                for stop in routes[node]:
                    if stop==target:
                        return level
                    for neigh in adj[stop]:
                        if neigh not in visited:
                            visited[neigh]=1
                            q.append(neigh)
                n-=1
        return -1
                    


        