class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ans=0
        maxlen=0
        temp=[]
        w=len(s)
        dp=[[None]* (w+1) for _ in range(w+1)]
        def palin(s,i,j):
            if dp[i][j] != None:
                return dp[i][j]
            if i>j:
                return 0
            if i==j:
                return 1
            if s[i]==s[j]:
                return 2+ palin(s,i+1,j-1)
            else:
                a=palin(s,i+1,j)
                b=palin(s,i,j-1)
            dp[i][j]=max(a,b)
            return max(a,b)
        return palin(s,0,len(s)-1)
            