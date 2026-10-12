class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp={}
        def minimum(i,j):
            if i>=len(s1):
                res1=0
                for t in range(j,len(s2)):
                    res1+=ord(s2[t])
                return res1

            if j >= len(s2):
                res = 0
                for k in range(i, len(s1)):
                    res += ord(s1[k])
                return res
            state=(i,j)
            if state in dp:
                return dp[state]
            if s1[i]==s2[j]:
                dp[state]= minimum(i+1,j+1)
                return dp[state]
            else:
                take=ord(s1[i]) + minimum(i+1, j)
                take1=ord(s2[j]) + minimum(i, j+1)
                dp[state]= min(take,take1)
                return dp[state]
        return minimum(0,0)