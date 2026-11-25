import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n=len(grid)
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        minheap=[]
        heapq.heappush(minheap,(grid[0][0],0,0))
        distance=[[float('inf')] * n for _ in range(n)]
        distance[0][0] = grid[0][0]
        while minheap:
            dist,row,col=heapq.heappop(minheap)

            if dist>distance[row][col]:
                continue
            if row==n-1 and col==n-1:
                return dist
            for p,k in direction:
                nr=p+row
                nc=k+col
                if nr>=0 and nr<n and nc>=0 and nc<n:
                    if distance[row][col] < grid[nr][nc]:
                        if distance[nr][nc] > grid[nr][nc]:
                            distance[nr][nc]=grid[nr][nc]
                            heapq.heappush(minheap,(grid[nr][nc],nr,nc))
                        
                    elif distance[row][col]>=grid[nr][nc]:
                        if distance[nr][nc] > distance[row][col]:
                            distance[nr][nc]=distance[row][col]
                            heapq.heappush(minheap,(distance[row][col],nr,nc))
        