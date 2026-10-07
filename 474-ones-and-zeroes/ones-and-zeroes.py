class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        count = []

        for s in strs:
            zero = 0
            one = 0

            for c in s:
                if c == "0":
                    zero += 1
                else:
                    one += 1

            count.append((zero, one))
        dp={}
        def sub(i,m,n):
            if i>=len(count):
                return 0
            state=(i,m,n)
            if state in dp:
                return dp[state]
            take=float('-inf')
            if count[i][0]<=m and count[i][1]<=n:
                take=1+sub(i+1,m-count[i][0],n-count[i][1])
            skip=sub(i+1,m,n)
            dp[state]= max(take,skip)
            return dp[state]
        return sub(0,m,n)
        

       