class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[0] * (n) for _ in range(m)]
        count=0
        dp=[[-1] * (n+1) for _ in range(m+1)]
        def cal(i,j):
           
            if i<0 or i>=m or j<0 or j>=n:
                return 0

            if i==m-1 and j==n-1:
                
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            original=grid[i][j]
            a=0
            b=0
            if i+1< m and grid[i+1][j] != "#":
                grid[i][j]="#"
                a=cal(i+1,j)
            if j+1<n and grid[i][j+1] !="#":
                grid[i][j]="#"
                b=cal(i,j+1)
            
            grid[i][j]=original
            dp[i][j]=a+b
            return a+b
        return cal(0,0)
        