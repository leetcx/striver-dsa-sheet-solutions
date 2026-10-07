class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[0] * len(s) for _ in range (len(s))]
        for l in range(1,len(s)+1):
            for i in range(n-l+1):
                j=i+l-1
                if i==j:
                    dp[i][j]= 1
                    continue
                if s[i]==s[j]:
                    dp[i][j]= 2+dp[i+1][j-1]
                else:
                    take1=dp[i+1][j]
                    take2=dp[i][j-1]
                    dp[i][j]= max(take1,take2)
        return dp[0][len(s)-1]