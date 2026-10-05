class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        p=len(text1)
        q=len(text2)
        dp=[[-1] * (q+1) for _ in range(p+1)]
        def print(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            if  i>=0 and i<p and j>=0 and j<q and dp[i][j] != -1:
                return dp[i][j]
            take=0
            skip1=0
            skip2=0
            if text1[i]==text2[j]:
                take=1+print(i+1,j+1)
                
            else:
                skip1=print(i+1,j)
                skip2=print(i,j+1)
            dp[i][j]= max(take,skip1,skip2)
            return dp[i][j]
        return print(0,0)