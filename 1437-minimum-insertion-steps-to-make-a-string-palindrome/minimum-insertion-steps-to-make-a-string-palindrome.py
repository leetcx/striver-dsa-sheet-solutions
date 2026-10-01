class Solution:
    def minInsertions(self, s: str) -> int:
        dp=[[-1]*(len(s)+1) for _ in range(len(s)+1)]
        def solve(i,j,s):
            if dp[i][j] != -1:
                return dp[i][j]
            if i>=j:
                return 0
            if s[i]==s[j]:
                return solve(i+1,j-1,s)
            else:
                a=1+solve(i+1,j,s)
                b=1+solve(i,j-1,s)
            dp[i][j]= min (a,b)
            return min(a,b)
        return solve(0,len(s)-1,s)