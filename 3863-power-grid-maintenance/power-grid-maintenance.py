
from collections import deque
from sortedcontainers import SortedList

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
                set1[p] = SortedList(z)
                p += 1

        component = [0] * (c+1)

        for key, value in set1.items():
            for node in value:
                component[node] = key

        ans = []

        for u, v in queries:
            key = component[v]

            if u == 1:
                if v in set1[key]:
                    ans.append(v)
                elif set1[key]:
                    ans.append(set1[key][0])
                else:
                    ans.append(-1)
            else:
                set1[key].discard(v)

        return ans
