from collections import deque
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        q.append((0,0,k))
        visited=set()
        visited.add((0, 0, k))
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        level=0
        def isvalid(r,c):
            if r<0 or r>=n or c<0 or c>=m:
                return False
            return True
        level=0
        while q:
            
            z=len(q)
            while z>0:
                i,j,k=q.popleft()
                if k<0:
                    return -1
                if i==n-1 and j==m-1:
                    return level
                for dx,dy in direction:
                    nr=i+dx
                    nc=j+dy

                    if isvalid(nr,nc):
                        nk=k-grid[nr][nc]
                        state=(nr,nc,nk)
                        if nk>=0 and state not in visited:
                            q.append(state)
                            visited.add(state)
            
                z-=1
            level+=1
        return -1
                

                
