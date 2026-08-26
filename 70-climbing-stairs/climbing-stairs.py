class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1] * n
        def cal(i,n):
            nonlocal dp
            if i==n:
                return 1
            if i>n:
                return 0
            if dp[i] != -1:
                return dp[i]
            a=cal(i+1,n)
            b=cal(i+2,n)
            ans=a+b
            dp[i]=ans
            return ans
        return cal(0,n)
