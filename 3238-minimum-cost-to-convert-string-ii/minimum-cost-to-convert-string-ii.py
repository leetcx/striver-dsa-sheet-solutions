
import heapq
from functools import lru_cache

class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str],
                    cost: List[int]) -> int:

        adj = {u: [] for u in set(original + changed)}

        for i in range(len(original)):
            adj[original[i]].append((changed[i], cost[i]))

        length = set()
        for u in original:
            length.add(len(u))

        def dijkstra(u, v):
            minheap = []
            heapq.heappush(minheap, (0, u))

            distance = {node: float('inf') for node in adj}
            distance[u] = 0

            while minheap:
                dist, node = heapq.heappop(minheap)

                if dist > distance[node]:
                    continue

                if node == v:
                    return dist

                for neigh, wt in adj.get(node, []):
                    newdist = dist + wt

                    if newdist < distance.get(neigh, float('inf')):
                        distance[neigh] = newdist
                        heapq.heappush(minheap, (newdist, neigh))

            return float('inf')

        n = len(source)


        dp1={}
        def dp(i):
            if i >= n:
                return 0
            if i in dp1:
                return dp1[i]
            ans = float('inf')

            if source[i] == target[i]:
                ans= dp(i + 1)

            for l in length:
                nr = i + l

                if nr <= n:
                    s = source[i:nr]
                    t = target[i:nr]
                    if s in original:
                        c = dijkstra(s, t)

                        if c != float('inf'):
                            ans = min(ans, c + dp(nr))
            dp1[i]=ans
            return ans

        result = dp(0)

        return -1 if result == float('inf') else result
