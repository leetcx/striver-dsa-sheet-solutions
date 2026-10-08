class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
        def count(i):

            if i>=len(s):
                return 1
            if s[i]=="0":
                return 0
            state=(i)
            if state in dp:
                return dp[state]
            nums=0
            take=0
            for j in range(i,len(s)):
                nums=nums*10+int(s[j])
                if nums>26:
                    break
                take+=count(j+1)
            dp[state]= take
            return take
        return count(0)
        
