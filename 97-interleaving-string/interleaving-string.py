class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp={}
        if len(s1)+len(s2) != len(s3):
            return False
        def check(i,j,k):
            if k>=len(s3):
                return True

            if i >= len(s1) and j >= len(s2):
                return False
            if i >= len(s1):
                if s2[j] == s3[k]:
                    return check(i, j+1, k+1)
                return False

            if j >= len(s2):
                if s1[i] == s3[k]:
                    return check(i+1, j, k+1)
                return False
            if s1[i] != s3[k] and s2[j] != s3[k]:
                return False
            state=(i,j,k)
            if state in dp:
                return dp[state]
            
            if s1[i]==s2[j]==s3[k]:
                take1=check(i+1,j,k+1)
                take2=check(i,j+1,k+1)
                dp[state]= take1 or take2
                return dp[state]
            elif s1[i]==s3[k]:
                take4=check(i+1,j,k+1)
                dp[state]= take4
                return dp[state]
            elif s2[j]==s3[k]:
                take5=check(i,j+1,k+1)
                dp[state]= take5
                return dp[state]
        return check(0,0,0)