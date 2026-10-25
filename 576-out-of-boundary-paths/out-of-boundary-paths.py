class Solution:
    def findPaths(self, m: int, n: int, maxmove: int, startrow: int, startcol: int) -> int:
        dp={}
        def total(startrow,startcol,maxmove):
            if maxmove>=0 and (startrow<0 or startrow>=m or startcol<0 or startcol>=n):
                return 1
            if maxmove<=0:
                return 0
            state=(startrow,startcol,maxmove)
            if state in dp:
                return dp[state]
            right=0
            left=0
            down=0
            up=0
            right+=total(startrow,startcol+1,maxmove-1)
            left+=total(startrow,startcol-1,maxmove-1)
            down+=total(startrow+1,startcol,maxmove-1)
            up+=total(startrow-1,startcol,maxmove-1)
            dp[state]= right+left+down+up
            return dp[state] % ((10**9)+7)
        return total(startrow,startcol,maxmove) % ((10**9)+7)