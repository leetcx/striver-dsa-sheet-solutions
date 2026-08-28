class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[[-1] *(n+1) for _ in range(n+1)]
        def path(i,n):
            if n==0:
                return 1
            if dp[i][n] != -1:
                return dp[i][n]
            if n>=2:
                a=path(i+1,n-1)
                b=path(i+2,n-2)
                dp[i][n]=a+b
            elif n==1:
                dp[i][n]=path(i+1,n-1)
            
            return dp[i][n]
        return path(1,n)