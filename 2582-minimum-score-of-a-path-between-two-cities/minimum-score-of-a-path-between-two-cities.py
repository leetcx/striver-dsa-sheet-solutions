import heapq

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        heap = [(float('inf'), 1)]
        visited = set()

        while heap:
            score, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            for nei, w in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (min(score, w), nei))

        return min(
            w
            for u, v, w in roads
            if u in visited and v in visited
        )