import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n=len(grid)
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        minheap=[]
        heapq.heappush(minheap,(grid[0][0],0,0))
        distance=[[float('inf')] * n for _ in range(n)]
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
                    newdist = dist

                    if grid[nr][nc] > dist:
                        newdist = grid[nr][nc]

                    if distance[nr][nc] > newdist:
                        distance[nr][nc] = newdist
                        heapq.heappush(minheap, (newdist, nr, nc))