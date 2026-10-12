class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        def do(i,j):
            if j>=len(t):
                return 1
            if i>=len(s):
                return 0
            state=(i,j)
            if state in dp:
                return dp[state]
            take=0
            take2=0
            if s[i] != t[j]:
                dp[state]= do(i+1,j)
                return dp[state]
            
           
            else:
                
                take+=do(i+1,j+1)
                take2+=do(i+1,j)
                dp[state]= take+take2
                return dp[state]
        return do(0,0)
        
        
