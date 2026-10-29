class Solution:
    def waysToReachStair(self, k: int) -> int:
        dp={}
        def ways(stair,jump,used):
            if stair==k:
                result=1
            else:
                result=0
            if stair>k+1:
                return 0
            state=(stair,jump,used)
            if state in dp:
                return dp[state]
            take=0
            skip=0
            if used==False and stair>0:
                take+=ways(stair-1,jump,True)
            skip+=ways(stair+(2**jump),jump+1,False)
            dp[state]= result+take+skip
            return dp[state]
        return ways(1,0,False)
        
            
            