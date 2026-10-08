class Solution:
    def minInsertions(self, s: str) -> int:
        z=len(s)
        dp=[[0] * (z+1) for _ in range(z+1)]
        for l in range(1,z+1):
            for i in range(z-l+1):
                j=i+l-1
                take1=float('inf')
                take2=float('inf')
                take3=float('inf')

                if s[i]==s[j]:
                    take1=dp[i+1][j-1]
                else:
                    take2=1+dp[i+1][j]
                    take3=1+dp[i][j-1]
                dp[i][j]= min(take1,take2,take3)
        return dp[0][z-1]
            