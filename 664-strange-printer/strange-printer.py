class Solution:
    def strangePrinter(self, s: str) -> int:
        dp={}
        def solve(l,r):
            if l==r:
                return 1
            if l>r:
                return 0
            state=(l,r)
            if state in dp:
                return dp[state]
            i=l+1
            while i <= r and s[i]==s[l]:
                i+=1
            if i==r+1:
                dp[state]=1
                return 1
            basic=1+solve(i,r)
            ans=0
            lalach=float('inf')
            for j in range(i,r+1):
                if s[j]==s[l]:
                    ans=solve(i,j-1)+solve(j,r)
                    lalach=min(lalach,ans)
            dp[state]= min(lalach,basic)
            return dp[state]
        return solve(0,len(s)-1)