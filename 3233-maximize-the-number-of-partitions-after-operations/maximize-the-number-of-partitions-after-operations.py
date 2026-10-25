from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        dp={}
        @lru_cache(None)
        def maxi(i,mask,canchange):
            if i==len(s):
                return 1
            state=(i,mask,canchange)
            if state in dp:
                return dp[state]
            bit=1<<(ord(s[i])-ord('a'))
            newmask= mask | bit
            ans=0
            if newmask.bit_count()<=k:
                ans=max(ans,maxi(i+1,newmask,canchange))
            else:
                ans=max(ans,1+maxi(i+1,bit,canchange))
            if canchange==True:
                for ch in range(26):
                    bit=1<<ch
                    newmask=mask | bit
                    if newmask.bit_count() <=k:
                        ans=max(ans,maxi(i+1,newmask,False))
                    else:
                        ans=max(ans,1+maxi(i+1,bit,False))
            dp[state]= ans
            return dp[state]
        return maxi(0,0,True)