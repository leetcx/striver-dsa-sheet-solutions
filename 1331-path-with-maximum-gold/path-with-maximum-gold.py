class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        maxpath=0
        m=len(grid)
        n=len(grid[0])
        pathsum=0
        ans=0

        def isvalid(row,col):
            if row+1<m and (grid[row+1][col] != -999 and grid[row+1][col]!= 0):
                return True
            if col+1<n and (grid[row][col+1] != -999 and grid[row][col+1]!= 0):
                return True
            if col-1>=0 and (grid[row][col-1] != -999 and grid[row][col-1]!= 0):
                return True
            if row-1>=0 and (grid[row-1][col] != -999 and grid[row-1][col]!= 0):
                return True
            return False

        def cal(grid,row,col):
            nonlocal m
            nonlocal n
            nonlocal maxpath
            nonlocal pathsum
            nonlocal ans

            original=grid[row][col]
            pathsum+=original
            grid[row][col]=-999

            if not isvalid(row,col):
                if pathsum>maxpath:
                    ans=pathsum
                    maxpath=pathsum

                grid[row][col]=original
                pathsum-=original
                return

            if row+1<m and (grid[row+1][col] != -999 and grid[row+1][col]!= 0):
                cal(grid,row+1,col)

            if col+1<n and (grid[row][col+1] != -999 and grid[row][col+1]!= 0):
                cal(grid,row,col+1)

            if col-1>=0 and (grid[row][col-1] != -999 and grid[row][col-1]!= 0):
                cal(grid,row,col-1)

            if row-1>=0 and (grid[row-1][col] != -999 and grid[row-1][col]!= 0):
                cal(grid,row-1,col)

            grid[row][col]=original
            pathsum-=original

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 or grid[i][j]==-999:
                    continue

                cal(grid,i,j)

        return ans