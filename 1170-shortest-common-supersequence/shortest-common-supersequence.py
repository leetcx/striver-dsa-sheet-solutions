class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m=len(s1)
        n=len(s2)
        dp=[[0]* (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=1+ min(dp[i-1][j],dp[i][j-1])
        lcs=[]
        while i>0 and j>0:
            if s1[i-1] == s2[j-1]:
                lcs.append(s1[i-1])
                i-=1
                j-=1
            else:
                
                if dp[i-1][j] < dp[i][j-1]:
                    lcs.append(s1[i-1])
                    i-=1
                else:
                    lcs.append(s2[j-1])
                    j-=1
        if i==0 and j !=0:
            lcs.append(s2[0:j])
        elif i!=0 and j==0:
            lcs.append(s1[0:i])
        lcs.reverse()
        mp="".join(lcs)
        return mp
