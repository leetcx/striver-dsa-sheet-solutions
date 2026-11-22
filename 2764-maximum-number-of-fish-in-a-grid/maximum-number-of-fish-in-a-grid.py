from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = [[False] * n for _ in range(m)]

        def bfs(i, j):
            ans = grid[i][j]
            q = deque()
            q.append((i, j, grid[i][j]))
            visited[i][j] = True

            while q:
                row, col, value = q.popleft()

                for p, k in direction:
                    nr = p + row
                    nc = k + col

                    if 0 <= nr < m and 0 <= nc < n:
                        if not visited[nr][nc] and grid[nr][nc] > 0:
                            visited[nr][nc] = True
                            ans += grid[nr][nc]
                            q.append((nr, nc, grid[nr][nc]))

            return ans

        result = float('-inf')

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    result = max(result, bfs(i, j))

        return result if result != float('-inf') else 0