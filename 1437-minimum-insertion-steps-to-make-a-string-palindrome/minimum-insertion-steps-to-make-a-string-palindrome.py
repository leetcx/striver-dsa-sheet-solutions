class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=l+i-1
                if i==j:
                    dp[i][j]=0
                elif s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]
                else:
                
                    dp[i][j]= 1+ min (dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
            