
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = []
        temp = []

        def backtrack(i):
            if i >= n:
                ans.append(temp.copy())
                return

            temp.append(i)
            backtrack(i + 1)
            temp.pop()

            backtrack(i + 1)

        backtrack(0)

        count = 0

        for subset in ans:
            active = set(subset)

            dist = [[float('inf')] * n for _ in range(n)]

            for i in range(n):
                dist[i][i] = 0

            for u, v, w in roads:
                if u in active and v in active:
                    dist[u][v] = min(dist[u][v], w)
                    dist[v][u] = min(dist[v][u], w)

            for k in active:
                for i in active:
                    for j in active:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][k] + dist[k][j]
                        )

            valid = True

            for i in active:
                for j in active:
                    if dist[i][j] > maxDistance:
                        valid = False
                        break
                if not valid:
                    break

            if valid:
                count += 1

        return count
