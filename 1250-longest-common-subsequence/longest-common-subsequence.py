class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n=len(t1)
        m=len(t2)
        dp=[[-1] * (m+1) for _ in range(n+1)]
        def chill(i,j):
            if i==n or j==m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if t1[i] == t2[j]:
                total=1+ chill(i+1,j+1)
                dp[i][j]=total
            else:
                a=chill(i+1,j)
                b=chill(i,j+1)
                total=max(a,b)
                dp[i][j]=total
            return total
        return chill(0,0)