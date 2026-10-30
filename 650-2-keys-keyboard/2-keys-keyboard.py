class Solution:
    def minSteps(self, n: int) -> int:
        dp={}
        def total(i,copy):
            if i==n:
                return 0
            if i > n:
                return float('inf')
            state=(i,copy)
            if state in dp:
                return dp[state]
            if copy != i:
                copyall = 1 + total(i, i)
            else:
                copyall = float('inf')
            if copy > 0:
                paste = 1 + total(i + copy, copy)
            else:
                paste = float('inf')
            dp[state]= min(copyall,paste)
            return dp[state]
        return total(1,0)

                