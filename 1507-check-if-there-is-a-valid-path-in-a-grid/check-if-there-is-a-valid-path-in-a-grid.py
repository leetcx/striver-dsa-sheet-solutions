from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        directionfor1 = [(0,-1),(0,1)]
        directionfor2 = [(-1,0),(1,0)]
        directionfor3 = [(0,-1),(1,0)]
        directionfor4 = [(0,1),(1,0)]
        directionfor5 = [(-1,0),(0,-1)]
        directionfor6 = [(-1,0),(0,1)]

        m = len(grid)
        n = len(grid[0])

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited = set()
            visited.add((i,j))

            while q:
                row,col = q.popleft()

                if row == m-1 and col == n-1:
                    return True

                if grid[row][col] == 1:
                    directions = directionfor1
                elif grid[row][col] == 2:
                    directions = directionfor2
                elif grid[row][col] == 3:
                    directions = directionfor3
                elif grid[row][col] == 4:
                    directions = directionfor4
                elif grid[row][col] == 5:
                    directions = directionfor5
                else:
                    directions = directionfor6

                for p,k in directions:
                    nr = row+p
                    nc = col+k

                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            direction_for_neighbor = directionfor1
                        elif grid[nr][nc] == 2:
                            direction_for_neighbor = directionfor2
                        elif grid[nr][nc] == 3:
                            direction_for_neighbor = directionfor3
                        elif grid[nr][nc] == 4:
                            direction_for_neighbor = directionfor4
                        elif grid[nr][nc] == 5:
                            direction_for_neighbor = directionfor5
                        else:
                            direction_for_neighbor = directionfor6

                        if (-p,-k) in direction_for_neighbor:
                            if (nr,nc) not in visited:
                                visited.add((nr,nc))
                                q.append((nr,nc))

            return False

        return bfs(0,0)