from collections import deque
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m=len(maze)
        n=len(maze[0])
        q=deque()
        q.append((entrance[0],entrance[1]))
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        level=0
        maze[entrance[0]][entrance[1]] = "+"
        while q:
            z=len(q)
            while z>0:
                i,j=q.popleft()
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and [i,j] != entrance:
                    return level
                for p in direction:
                    nr=i+p[0]
                    nc=j+p[1]
                    if 0<=nr<m and 0<=nc<n and maze[nr][nc]!="+":
                        maze[nr][nc]="+"
                        q.append((nr,nc))
                z-=1
            level+=1
        return -1
