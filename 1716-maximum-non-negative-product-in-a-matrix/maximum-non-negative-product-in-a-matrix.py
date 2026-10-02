class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        MOD= 10** 9 +7
        dp=[[-1] * (n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m - 1 and j == n - 1:
                    dp[m-1][n-1]=(grid[m-1][n-1],grid[m-1][n-1]) 
                    continue    
                maxval = float("-inf")
                minval = float("inf")
                if j+1<n:
                    rightmin, rightmax = dp[i][j+1]
                    maxval=max(maxval,grid[i][j] * rightmin,grid[i][j] * rightmax)
                    minval=min(minval,grid[i][j] * rightmin,grid[i][j] *rightmax)
                if i+1<m:
                    downmin, downmax = dp[i+1][j]
                    maxval=max(maxval,grid[i][j] * downmin,grid[i][j] * downmax)
                    minval=min(minval,grid[i][j] * downmin,grid[i][j] *downmax)

           

            
            

                dp[i][j]=minval, maxval
                

        minval, maxval = dp[0][0]
        if maxval<0:
            return -1
        return maxval % MOD