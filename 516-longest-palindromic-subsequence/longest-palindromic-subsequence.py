class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ans=[]
        n=len(s)
        maxlen=float('-inf')
        t=[[1] * (n+1) for _ in range(n+1)]
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if i==j:
                    t[i][j]=1
                elif i+1==j:
                    if s[i]==s[j]:
                        t[i][j]=2
                else:
                    if s[i]==s[j]:
                        t[i][j]=2+ t[i+1][j-1]
                    else:
                        t[i][j]=max(t[i+1][j],t[i][j-1])

        return t[0][n-1]
        
        
           
        