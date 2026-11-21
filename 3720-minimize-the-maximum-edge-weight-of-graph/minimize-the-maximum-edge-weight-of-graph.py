from collections import deque

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:

        if n > 1 and threshold == 0:
            return -1

        weights = sorted(set(w for u, v, w in edges))

        def bfs(wt):
            q = deque()
            adj = [[] for _ in range(n)]

            for u, v, w in edges:
                if w <= wt:
                    adj[v].append(u)

            q.append(0)
            visited = [False] * n
            visited[0] = True
            count = 1

            while q:
                node = q.popleft()

                for neigh in adj[node]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        count += 1
                        q.append(neigh)

            return count == n

        low = 0
        high = len(weights) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if bfs(weights[mid]):
                ans = weights[mid]
                high = mid - 1
            else:
                low = mid + 1

        return ans