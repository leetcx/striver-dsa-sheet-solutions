class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp={}
        def doit(i,prev,freqq,k):
            if k<0:
                return float('inf')
            if i>=len(s):
                return 0
            state=(i,prev,freqq,k)
            if state in dp:
                return dp[state]
            delete=doit(i+1,prev,freqq,k-1)
            keep=0
            if s[i]!=prev:
                keep=1+doit(i+1,s[i],1,k)
            else:
                onemore=0
                if freqq==1 or freqq==9 or freqq==99:
                    onemore=1
                keep=onemore+doit(i+1,prev,freqq+1,k)
            dp[state]= min(keep,delete)
            return dp[state]
        return doit(0,'',0,k)