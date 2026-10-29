class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def countsteps(i,k):
            clock=abs(i-k)
            anti=abs(len(ring)-clock)
            return min(clock,anti)
        dp=[[-1] * (len(key)+1) for _ in range(len(ring)+1)]
        def ways(i,j):
            if j>=len(key):
                return 0
            
            if dp[i][j] !=-1:
                
                return dp[i][j]
            result=float('inf')
            totalsteps=float('inf')
            for k in range(len(ring)):
                if ring[k]==key[j] :
                    steps=countsteps(i,k) 
                    totalsteps=steps+1+ways(k,j+1)
                    result=min(result,totalsteps)
            dp[i][j]= result
            return dp[i][j]
        return ways(0,0)
                  