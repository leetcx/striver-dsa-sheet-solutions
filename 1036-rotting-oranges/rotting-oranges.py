from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        if fresh==0:
            return 0
        time=0
        while q:
            p=len(q)
            while p>0:
                i,j=q.popleft()
                if i+1<m and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    fresh-=1
                    q.append((i+1,j))
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    fresh-=1
                    q.append((i-1,j))
                if j+1<n and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    fresh-=1
                    q.append((i,j+1))
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    fresh-=1
                    q.append((i,j-1))
                p-=1
            if q:
                time+=1
        if fresh==0:
            return time
        return -1



