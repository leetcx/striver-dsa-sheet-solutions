class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n=len(piles)
        dp={}
        def maxpiles(i,M,person):
            if i>=len(piles):
                return 0
            state=(i,M,person)
            if state in dp:
                return dp[state]
            if person==1:
                result=-1
            else:
                result=float('inf')
            total=0
            for x in range(1,min(n-i,2*M)+1):
                total+=piles[i+x-1]
                if person==1:

                   
                    result=max(result,total+maxpiles(i+x,max(M,x),0))
                else:
                    result=min(result,maxpiles(i+x,max(M,x),1))
            dp[state]= result
            return dp[state]
        return maxpiles(0,1,1)
       

                