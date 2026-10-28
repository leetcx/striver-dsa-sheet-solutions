class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = [[False] * 102 for _ in range(102)]
        n=len(s)
        dp[n][0]=True
        for i in range(n-1,-1,-1):
            for open in range(n+1):
                if open<0:
                    dp[i][open]==False
                
            
            
                if s[i] == "*":
                    dp[i][open] = dp[i + 1][open] or dp[i + 1][ open + 1] 
                    if open>0:
                        dp[i][open] = dp[i][open] or dp[i + 1][open - 1]
                
                elif s[i] == "(":
                    dp[i][open] = dp[i + 1][ open + 1]
                elif s[i] == ")":
                    if open>0:
                        dp[i][open] = dp[i + 1][ open-1]

           
        return dp[0][0]
