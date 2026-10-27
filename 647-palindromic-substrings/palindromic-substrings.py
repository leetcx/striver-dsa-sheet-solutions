class Solution:
    def countSubstrings(self, s: str) -> int:
        dp={}
        def istrue(j,i):
            if i<=j:
                return True
            state=(i,j)
            if state in dp:
                return dp[state]
            if s[i]==s[j]:
                if istrue(j+1,i-1):
                    dp[state]= True
                    return True
                dp[state]= False
                return False
            else:
                dp[state]=False
                return False
        c=0
        for i in range(len(s)):
            for j in range(i+1):
                if istrue(j,i):
                    c+=1
        return c
                
            