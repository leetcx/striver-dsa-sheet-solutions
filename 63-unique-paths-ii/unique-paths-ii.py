class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0] * (n) for _ in range(m)]
        
        for z in range(m):
            if grid[z][0]==1:
                dp[z][0]=0
            elif z>0 and dp[z-1][0]==0:
                dp[z][0]=0
            else:
                dp[z][0]=1
        for z in range(n):
            if grid[0][z]==1:
                dp[0][z]=0
            elif z>0 and dp[0][z-1]==0:
                dp[0][z]=0
            else:
                dp[0][z]=1
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]==1:
                    dp[i][j]=0
                    continue
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]
        


