class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        p=len(text1)
        q=len(text2)
        dp=[[-1] * (q+1) for _ in range(p+1)]
        for t in range(p+1):
            dp[t][0]=0
        for t in range(q+1):
            dp[0][t]=0

        for i in range(1,p+1):
            for j in range(1,q+1):
                
                take=0
                skip1=0
                skip2=0
                
                if text1[i-1]==text2[j-1]:
                    take=1+dp[i-1][j-1]
                
                else:
                    skip1=dp[i-1][j]
                    skip2=dp[i][j-1]
                dp[i][j]= max(take,skip1,skip2)
           
        return dp[p][q]