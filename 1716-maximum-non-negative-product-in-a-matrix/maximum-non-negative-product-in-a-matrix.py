class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        MOD= 10** 9 +7
        dp=[[-1] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j]=(grid[i][j],grid[i][j]) 
                    continue    
                maxval = float("-inf")
                minval = float("inf")
                if j-1>=0:
                    rightmin, rightmax = dp[i][j-1]
                    maxval=max(maxval,grid[i][j] * rightmin,grid[i][j] * rightmax)
                    minval=min(minval,grid[i][j] * rightmin,grid[i][j] *rightmax)
                if i-1>=0:
                    downmin, downmax = dp[i-1][j]
                    maxval=max(maxval,grid[i][j] * downmin,grid[i][j] * downmax)
                    minval=min(minval,grid[i][j] * downmin,grid[i][j] *downmax)

           

            
            

                dp[i][j]=minval, maxval
                

        minval, maxval = dp[m-1][n-1]
        if maxval<0:
            return -1
        return maxval % MOD