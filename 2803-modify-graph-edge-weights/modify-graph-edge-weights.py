import heapq

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):

        def bfs(edges, source, dest):
            adj = [[] for _ in range(n)]

            for u, v, w in edges:
                if w == -1:
                    continue
                adj[u].append((v, w))
                adj[v].append((u, w))

            minheap = []
            distance = [float('inf')] * n
            heapq.heappush(minheap, (0, source))
            distance[source] = 0

            while minheap:
                dist, node = heapq.heappop(minheap)

                if dist > distance[node]:
                    continue

                for neigh in adj[node]:
                    nody = neigh[0]
                    wt = neigh[1]

                    if dist + wt < distance[nody]:
                        distance[nody] = dist + wt
                        heapq.heappush(minheap, (dist + wt, nody))

            return distance[dest]
        
        normal = bfs(edges, source, destination)
    
        if normal != float('inf') and normal < target:
            return []

        if normal == target:
            for i in range(len(edges)):
                if edges[i][2] == -1:
                    edges[i][2] = 2 * 10**9
            return edges

        if  normal > target:
            found=False
            for i in range(len(edges)):
                if edges[i][2] == -1:
                    edges[i][2] = 1
                    sp = bfs(edges, source, destination)

                    if sp <= target:
                        edges[i][2] += target - sp
                        found=True
                        break
        if not found:
            return []

        for i in range(len(edges)):
            if edges[i][2] == -1:
                edges[i][2] = 2 * 10**9

        return edges