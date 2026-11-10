from collections import deque

class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        adj1 = [[] for _ in range(len(edges1) + 1)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        adj2 = [[] for _ in range(len(edges2) + 1)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        start = 0
        farthest = start
        n = len(edges1) + 1
        m = len(edges2) + 1

        visited = [False] * n
        visited[start] = True
        q = deque()
        q.append(start)
        dist = [0] * n

        while q:
            node = q.popleft()
            if dist[node] > dist[farthest]:
                farthest = node

            for neigh in adj1[node]:
                if visited[neigh] == False:
                    dist[neigh] = 1 + dist[node]
                    visited[neigh] = True
                    q.append(neigh)

        visited1 = [False] * n
        distance = [0] * n
        visited1[farthest] = True
        z = deque()
        z.append(farthest)

        while z:
            node1 = z.popleft()
            for neigh in adj1[node1]:
                if visited1[neigh] == False:
                    distance[neigh] = 1 + distance[node1]
                    visited1[neigh] = True
                    z.append(neigh)

        diameter1 = max(distance)

        start = 0
        farthest = start

        visited = [False] * m
        visited[start] = True
        q = deque()
        q.append(start)
        dist1 = [0] * m

        while q:
            node = q.popleft()
            if dist1[node] > dist1[farthest]:
                farthest = node

            for neigh in adj2[node]:
                if visited[neigh] == False:
                    dist1[neigh] = 1 + dist1[node]
                    visited[neigh] = True
                    q.append(neigh)

        visited1 = [False] * m
        distance1 = [0] * m
        visited1[farthest] = True
        z = deque()
        z.append(farthest)

        while z:
            node1 = z.popleft()
            for neigh in adj2[node1]:
                if visited1[neigh] == False:
                    distance1[neigh] = 1 + distance1[node1]
                    visited1[neigh] = True
                    z.append(neigh)

        diameter2 = max(distance1)

        return max(
            diameter1,
            diameter2,
            (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1
        )