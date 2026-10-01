class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*(n) for _ in range(m)]
       
        for i in range(m):
            for j in range(n):
                if i-1>=0 and j-1>=0 :
                    dp[i][j]=grid[i][j] + min(dp[i-1][j],dp[i][j-1])
                elif i-1>=0 and j-1<0:
                    dp[i][j]=grid[i][j]+ dp[i-1][j]
                elif j-1>=0 and i-1<0:
                    dp[i][j]=grid[i][j]+ dp[i][j-1]
                elif i-1<0 and j-1<0 :
                    dp[i][j]=grid[i][j]
        return dp[m-1][n-1]
        

        