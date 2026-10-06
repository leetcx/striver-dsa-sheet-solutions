class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
            
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                    continue
           
                downsum=float('inf')
                rightsum=float('inf')
                if i-1>=0 :
                    downsum=grid[i][j]+dp[i-1][j]
                if j-1>=0:
                    rightsum=grid[i][j]+dp[i][j-1]
                dp[i][j]= min(downsum,rightsum)
        return dp[m-1][n-1]
            