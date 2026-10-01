class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1] * (n+1) for _ in range(m+1)]
        def lesdo(i,j):
            if i>=m or i <0 or j>=n or j<0 or grid[i][j]==1 or grid[i][j]=="#":
                return 0
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j]!= -1:
                return dp[i][j]
            original=grid[i][j]
            grid[i][j]="#"
            right=lesdo(i,j+1)
            
            grid[i][j]="#"
            down=lesdo(i+1,j)
            grid[i][j]=original
            dp[i][j]= right+down
            return dp[i][j]
            
        return lesdo(0,0)



