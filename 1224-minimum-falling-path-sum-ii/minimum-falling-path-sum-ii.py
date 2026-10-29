class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        nextmincol1=-1
        nextmincol2=-1
        for j in range(n):
            if nextmincol1==-1 or grid[n-1][j]<=grid[n-1][nextmincol1]:
                nextmincol2=nextmincol1
                nextmincol1=j
               
            elif nextmincol2==-1 or grid[n-1][j]<=grid[n-1][nextmincol2]:
                nextmincol2=j
        for i in range(n - 2, -1, -1):
            mincol1=-1
            mincol2=-1
            for col in range(n):
                if col != nextmincol1:
                    grid[i][col]=grid[i][col]+grid[i+1][nextmincol1]
                else:
                    grid[i][col]=grid[i][col]+grid[i+1][nextmincol2]
                if mincol1==-1 or grid[i][col]<=grid[i][mincol1]:
                    
                    mincol2=mincol1
                    mincol1=col
                elif mincol2==-1 or grid[i][col]<=grid[i][mincol2]:
                    mincol2=col
            nextmincol1=mincol1
            nextmincol2=mincol2
        return min(grid[0])

                