
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstperson: int) -> list[int]:
        dict1={}
        meetings.sort(key=lambda x: x[2])
        for u,v,w in meetings:
            if w not in dict1:
                dict1[w]=[]
            dict1[w].append((u,v))
        known=[False] * n
        known[0]=True
        known[firstperson]=True
        for time in dict1:
            adj = defaultdict(list)

            for u, v in dict1[time]:
                adj[u].append(v)
                adj[v].append(u)
            visited=set()
            q=deque()
            for person in adj:
                if known[person]:
                    q.append(person)
                    visited.add(person)
            while q:
                node=q.popleft()
                for neigh in adj[node]:
                    if known[neigh]==False:
                        
                        q.append(neigh)
                        known[neigh]=True
        return [i for i in range(n) if known[i]]
                


        