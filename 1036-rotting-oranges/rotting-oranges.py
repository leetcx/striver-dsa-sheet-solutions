from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        fresh=0
        m=len(grid)
        n=len(grid[0])
        q=deque()
        visited=[[False]*n for _ in range(m)]
        time=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                    visited[i][j]=True
                if grid[i][j]==1:
                    fresh+=1
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
                        q.append((r,c))
                        fresh-=1
                        visited[r][c]= True
            if q:
                time+=1
                    
            
        if fresh>0:
            return -1
        return time

        