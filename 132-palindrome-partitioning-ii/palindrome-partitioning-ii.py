class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[[0] *(n+1) for _ in range(n+1)]
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=l+i-1
                if i==j:
                    dp[i][j]=True
                elif i+1==j:
                    if s[i]==s[j]:
                        dp[i][j]=True
                else:
                    if s[i]==s[j]:
                        dp[i][j]=dp[i+1][j-1]
       
       
        t=[-1] * (n+1)
        def backtrack(i):
            
            if i>=len(s):
               
                return 0
            if t[i] != -1:
                return t[i]
            
            ans=float('inf')
            for j in range(i,len(s)):
                if dp[i][j]:
                    cut=1+backtrack(j+1)
                    ans=min(cut,ans)
            t[i]=ans
            return ans
        return backtrack(0)-1
                
            
    
                
