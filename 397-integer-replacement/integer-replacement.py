class Solution:
    def integerReplacement(self, n: int) -> int:
        dp={}
        def mini(n):
            if n==1:
                return 0
            if n in dp:
                return dp[n]
            skippy=float('inf')
            take1=float('inf')
            take2=float('inf')
            if n%2==0:
                skippy=1+mini(n/2)
            else:
                take1=1+mini(n-1)
                take2=1+mini(n+1)
            dp[n]= min(skippy,take1,take2)
            return dp[n]
        return mini(n)
            
