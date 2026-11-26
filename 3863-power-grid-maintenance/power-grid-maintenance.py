
from collections import deque
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        set1 = {}
        adj = [[] for _ in range(c+1)]
        p = 0
        visited = [False] * (c+1)

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node, adj):
            q = deque()
            q.append(node)
            visited[node] = True
            temp = []

            while q:
                do = q.popleft()
                temp.append(do)

                for neigh in adj[do]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        q.append(neigh)

            return temp

        for i in range(1, c+1):
            if not visited[i]:
                z = bfs(i, adj)
                set1[p] = z
                p += 1

        component = [0] * (c+1)
        heaps = {}

        for key, value in set1.items():
            heaps[key] = value[:]
            heapq.heapify(heaps[key])

            for node in value:
                component[node] = key

        online = [True] * (c+1)
        ans = []

        for u, v in queries:
            if u == 1:
                if online[v]:
                    ans.append(v)
                else:
                    key = component[v]

                    while heaps[key] and not online[heaps[key][0]]:
                        heapq.heappop(heaps[key])

                    if heaps[key]:
                        ans.append(heaps[key][0])
                    else:
                        ans.append(-1)

            else:
                online[v] = False

        return ans
