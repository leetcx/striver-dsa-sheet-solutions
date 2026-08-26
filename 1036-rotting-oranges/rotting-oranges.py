from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        fresh=0
        time=0
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        visited=[[False]*n for _ in range(m)]
        for i in range(m):
            for j in  range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
                    visited[i][j]=True
        def valid(r,c,m,n):
            if r<0 or r>=m or c<0 or c>=n:
                return False
            return True
        while q:
            p=len(q)
            for i in range(p):
                row,col=q.popleft()
                for k in range(4):
                    r=row+x[k]
                    c=col+y[k]
                    if valid(r,c,m,n) and visited[r][c]==False and grid[r][c]==1:
                        fresh-=1
                        visited[r][c]=True
                        q.append((r,c))
            if q:
                time+=1
        if fresh>0:
            return -1
        return time
        