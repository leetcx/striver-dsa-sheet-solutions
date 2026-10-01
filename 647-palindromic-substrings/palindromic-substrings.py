class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        t=[[False] * (n+1) for _ in range(n+1)]
        count=0
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
                    count+=1
        return count
                
