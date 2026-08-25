from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        q=deque()
        visited=[[False] *n for _ in range(n)]
        if grid[0][0] ==1 or grid[n-1][n-1]==1:
            return -1
        x = [-1, -1, -1, 0, 0, 1, 1, 1]
        y = [-1,  0,  1,-1, 1,-1, 0, 1]
        res=1
        q.append((0,0))
        visited[0][0]=True
        def valid(r,c,n):
            if r<0 or r>=n or c<0 or c>=n:
                return False
            return True
        while q:
            p=len(q)
            for i in range(p):
                row,col=q.popleft()
                
                if row==n-1 and col==n-1:
                    return res
                for k in range(8):
                    r=row+x[k]
                    c=col+y[k]
                    if valid(r,c,n) and visited[r][c]==False and grid[r][c]==0:
                        q.append((r,c))
                        visited[r][c]=True
            res+=1
        return -1
        

