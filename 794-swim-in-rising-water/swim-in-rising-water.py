import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        m=len(grid)
        n=len(grid[0])
        res=[[float('inf') for _ in range(n)] for _ in range(m)]
        res[0][0]=grid[0][0]
        pq=[]
        heapq.heappush(pq,(grid[0][0],0,0))
        def valid(m,n,i,j):
            if i<0 or i>= m or j<0 or j>=n:
                return False
            return True
        while pq:
            money,row,col=heapq.heappop(pq)
            if money > res[row][col]:
                continue
            for k in range(4):
                r=row+x[k]
                c=col+y[k]
                if  not valid(m,n,r,c):
                    continue
                adji=max(money,grid[r][c])
                if adji < res[r][c]:
                    res[r][c]=adji
                
                    heapq.heappush(pq,(adji,r,c))
        return res[m-1][n-1]