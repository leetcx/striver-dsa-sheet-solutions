import heapq
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        minheap=[]
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        heapq.heappush(minheap,(0,0,0,grid[0][0]))
        cost=[[float('inf')] * n for _ in range(m)]
        cost[0][0]=0 
        visited=[[False] * n for _ in range(m)]
        while minheap:
            costy,row,col,sign=heapq.heappop(minheap)
            visited[row][col]=True
            if row==m-1 and col==n-1:
                return costy
            if costy>cost[row][col]:
                continue
            for p,k in direction:
                nr=row+p
                nc=col+k
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    
                    if sign==1:
                        checkcol=col+1
                        checkrow=row
                    elif sign==2:
                        checkcol=col-1
                        checkrow=row
                    elif sign==3:
                        checkrow=row+1
                        checkcol=col
                    else:
                        checkrow=row-1
                        checkcol=col
                    if not visited[nr][nc]:
                        
                        if nr==checkrow and nc==checkcol:
                            newcost=costy
                        else:
                            newcost=costy+1
                        if newcost<cost[nr][nc]:
                            cost[nr][nc]=newcost
                            heapq.heappush(minheap, (newcost, nr, nc,grid[nr][nc]))
                            
        return -1
                

                            

               