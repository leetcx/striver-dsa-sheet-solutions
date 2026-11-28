class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        visited=set()
        def hascycle(a,b):
            
            q=deque()
            q.append((a,b,-1,-1))
            visited.add((a,b))
            while q:
                row,col,p,l=q.popleft()
                for z,k in direction:
                    nr=row+z
                    nc=col+k
                    if nr>=0 and nr<m and nc>=0 and nc<n and grid[row][col]==grid[nr][nc]:
                        if (nr,nc) in visited and (nr, nc) != (p, l):
                            return True
                        elif (nr,nc) not in visited:
                            q.append((nr,nc,row,col))
                            visited.add((nr,nc))
            return False

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    if hascycle(i,j):
                        return True
        return False