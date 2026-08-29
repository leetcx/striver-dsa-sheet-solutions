class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n=len(t1)
        m=len(t2)
        t=max(n,m)
        dp=[[-1] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][m]=0
        for i in range(m+1):
            dp[n][i]=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if t1[i] == t2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    a=dp[i+1][j]
                    b=dp[i][j+1]
                    p=max(a,b)
                    dp[i][j]=p
        return dp[0][0]

        

            
            