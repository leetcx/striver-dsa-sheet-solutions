import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        minheap=[]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        healthreq=[[float('inf')] * n for _ in range(m)]
        healthreq[0][0]=grid[0][0]
        heapq.heappush(minheap,((grid[0][0]),0,0))
        while minheap:
            he,u,v=heapq.heappop(minheap)
            if he>healthreq[u][v]:
                continue
            for p in direction:
                nr=u+p[0]
                nc=v+p[1]
                if 0<=nr<m and 0<=nc<n:
                    if  healthreq[nr][nc]>he+grid[nr][nc]:
                        healthreq[nr][nc]=he+grid[nr][nc]
                        heapq.heappush(minheap,((he+grid[nr][nc]),nr,nc))
        return healthreq[m-1][n-1]<health
        



        