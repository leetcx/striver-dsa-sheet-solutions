
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n=len(grid)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        q=deque()
        q.append((0,0,1))
        steps=0
        grid[0][0]=1
        def isvalid(i,j):
            if i>=n or i<0 or j>=n or j<0:
                return False
            return True
        while q:
            i,j,dist=q.popleft()
            if i==n-1 and j==n-1:
                return dist
            for p,k in directions:
                nextrow=i+p
                nextcol=j+k
                if isvalid(nextrow,nextcol) and grid[nextrow][nextcol]==0:
                    steps+=1
                    q.append((nextrow,nextcol,dist+1))
                    grid[nextrow][nextcol]=1
        return -1
                    
            

        