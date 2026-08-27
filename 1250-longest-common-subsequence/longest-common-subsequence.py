class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n=len(t1)
        m=len(t2)
        dp=[[-1] *m for _ in range(n)]
        T=0
        def siu(i,j):
            nonlocal T
            if i == n or j==m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if t1[i]==t2[j]:
                dp[i][j]=1+siu(i+1,j+1)
                return dp[i][j]   
            else:
                c1=siu(i+1,j)
                c2=siu(i,j+1)
                T=max(c1,c2)
                dp[i][j]=T
            return T
        return siu(0,0)

