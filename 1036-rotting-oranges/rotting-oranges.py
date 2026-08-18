from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        q=deque()
        fresh=0
        time=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        def valid(i,j,m,n):
            if i<0 or i>=m or j<0 or j>=n:
                return False
            return True
        while q and fresh>0:
            p=len(q)
            while p:
                i,j=q.popleft()
                for k in range(0,4):
                    row=i+x[k]
                    col=j+y[k]
                    if valid(row,col,m,n) and grid[row][col]==1:
                        q.append((row,col))
                        grid[row][col]=-2
                        fresh-=1
                p-=1
            time+=1
        if fresh>0:
            return -1
        return time
               




