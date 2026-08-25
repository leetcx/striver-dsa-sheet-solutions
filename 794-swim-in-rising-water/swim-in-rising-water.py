import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        q=[]
        heapq.heappush(q,(grid[0][0],0,0))
        res = [[float('inf')] * n for _ in range(n)]
        res[0][0]=grid[0][0]
        def valid(r,c,n):
            if r<0 or r>=n or c<0 or c>=n:
                return False
            return True
        while q:
            dist,row,col=heapq.heappop(q)
            if row==n-1 and col==n-1:
                return dist
            if dist > res[row][col]:
                continue
            for k in range(4):
                r=row+x[k]
                c=col+y[k]
                if valid(r,c,n):
                    t=max(dist,grid[r][c])
                    if t< res[r][c]:
                        res[r][c]=t
                        heapq.heappush(q,(t,r,c))
        return res[n-1][n-1]