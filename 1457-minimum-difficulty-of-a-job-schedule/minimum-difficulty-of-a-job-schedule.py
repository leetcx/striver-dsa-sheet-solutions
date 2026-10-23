class Solution:
    def minDifficulty(self, job: list[int], d: int) -> int:
        if len(job)<d:
            return -1
        if len(job)==d:
            return sum(job)
        dp={}
        def aximum(i,d,currmax):
            if i >= len(job):
                if d == 0:
                    return 0
                return float('inf')
            if d <= 0:
                return float('inf')

            
            state=(i,d,currmax)
            if state in dp:
                return dp[state]
            currmax=max(currmax,job[i])
            continue1=aximum(i+1,d,currmax)
            move=0
            if d>0:
                move=currmax+aximum(i+1,d-1,float('-inf'))
            dp[state]= min(continue1,move)
            return dp[state]
        return aximum(0,d,float('-inf'))



        
        