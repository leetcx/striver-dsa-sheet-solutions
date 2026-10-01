class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=[]
        n=len(s)
        maxlen=float('-inf')
        t=[[False] * (n+1) for _ in range(n+1)]
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if i==j:
                    t[i][j]=True
                elif i+1==j:
                    if s[i]==s[j]:
                        t[i][j]=True
                else:
                    if s[i]==s[j]:
                        t[i][j]=t[i+1][j-1]
                if t[i][j]==True:
                    if j-i+1>maxlen:
                        ans= [s[i:j+1]]
                        maxlen=j-i+1
        z="".join(ans)
        return z
        
        
           