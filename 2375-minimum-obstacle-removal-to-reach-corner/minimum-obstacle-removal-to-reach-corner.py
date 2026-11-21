import heapq
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        minheap=[]
        heapq.heappush(minheap,(0,0,0))
        distance=[[float('inf')] *n for _ in range(m)]
        distance[0][0]=0
        while minheap:
            dist,row,col=heapq.heappop(minheap)
            if row==m-1 and col==n-1:
                return dist
            if dist>distance[row][col]:
                continue
            for p,q in direction:
                nr=row+p
                nc=col+q
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    if grid[nr][nc] ==1:
                        if distance[nr][nc]>dist+1:
                            distance[nr][nc]=dist+1
                            heapq.heappush(minheap,(dist+1,nr,nc))
                    else:
                        if distance[nr][nc]>dist:
                            distance[nr][nc]=dist
                            heapq.heappush(minheap,(dist,nr,nc))
        
            
        
        
        
