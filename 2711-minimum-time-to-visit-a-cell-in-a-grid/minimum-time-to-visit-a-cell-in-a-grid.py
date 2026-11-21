import heapq
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        minheap=[]
        direction=[(1,0),(0,1),(0,-1),(-1,0)]
        heapq.heappush(minheap,(0,0,0))
        distance=[[float('inf')] *n for _ in range(m)]
        distance[0][0]=0
        while minheap:
            time,row,col=heapq.heappop(minheap)
            if row==m-1 and col==n-1:
                return time
            if time>distance[row][col]:
                continue
            for p,k in direction:
                nr=p+row
                nc=k+col
                
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    newtime=time+1
                    if grid[nr][nc]>newtime:
                        newtime=grid[nr][nc]+((grid[nr][nc]-newtime) %2)
                    if distance[nr][nc]>newtime:
                        distance[nr][nc]=newtime
                        heapq.heappush(minheap,(newtime,nr,nc))
                   
        return -1
             
