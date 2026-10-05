class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1] * (n+1)
        def take(n):
            if n<0:
                return 0
            if n==0:
                return 1
            if dp[n] != -1:
                return dp[n]
            take1=take(n-1)
            take2=take(n-2)
            dp[n]=take1 + take2
            return dp[n]
        return take(n)