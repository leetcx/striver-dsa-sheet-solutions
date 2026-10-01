class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        dp=[[0] * (n) for _ in range(m)]
        if m==1 and n==1:
            return 1
        for z in range(1,m):
            dp[z][0]=1
        for l in range(1,n):
            dp[0][l]=1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+ dp[i][j-1]
        return dp[m-1][n-1]