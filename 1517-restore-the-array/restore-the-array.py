class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp=[-1] * (len(s)+1)
        def build(i):
            
            if i>=len(s):
                
                return 1
            if s[i]=="0":
                return 0
            if dp[i] != -1:
                return dp[i]
            take=0
            num=0
            for j in range(i,len(s)):
                
                num=num*10 + int(s[j])
                if num>k:
                    break
                take+=build(j+1)
                take=take% ((10**9)+7)
            dp[i]=take
            return take
        return build(0)
            
            