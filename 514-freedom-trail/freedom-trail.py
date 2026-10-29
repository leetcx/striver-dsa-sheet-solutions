class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def countsteps(i,k):
            clock=abs(i-k)
            anti=abs(len(ring)-clock)
            return min(clock,anti)
        dp={}
        def ways(i,j):
            if j>=len(key):
                return 0
            state=(i,j)
            if state in dp:
                return dp[state]
            result=float('inf')
            totalsteps=float('inf')
            for k in range(len(ring)):
                if ring[k]==key[j] :
                    steps=countsteps(i,k) 
                    totalsteps=steps+1+ways(k,j+1)
                    result=min(result,totalsteps)
            dp[state]= result
            return dp[state]
        return ways(0,0)
                  