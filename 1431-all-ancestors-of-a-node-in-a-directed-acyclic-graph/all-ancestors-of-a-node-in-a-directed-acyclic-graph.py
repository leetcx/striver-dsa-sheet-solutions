from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topoOrder = []

        # First pass: Topological Sort
        while q:
            curr = q.popleft()
            topoOrder.append(curr)

            for neigh in adj[curr]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    q.append(neigh)

        # Second pass: Propagate ancestors
        ancestors = [set() for _ in range(n)]

        for node in topoOrder:
            for neigh in adj[node]:
                ancestors[neigh].add(node)
                ancestors[neigh].update(ancestors[node])

        return [sorted(x) for x in ancestors]