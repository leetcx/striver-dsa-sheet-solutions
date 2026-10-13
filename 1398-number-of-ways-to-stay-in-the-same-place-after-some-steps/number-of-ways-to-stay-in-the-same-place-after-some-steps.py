class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp={}
        def lesdo(steps,i):
            if steps==0:
                if  i==0:
                    return 1
                return 0
            if i<0 or i>=arrLen:
                return 0
            state=(steps,i)
            if state in dp:
                return dp[state]
            
            move1=0
            move1+=lesdo(steps-1,i+1)
            move1+=lesdo(steps-1,i-1)
            move1+=lesdo(steps-1,i)
            dp[state]= move1
            return dp[state] %((10**9)+7)
        return lesdo(steps,0) %((10**9)+7)
            