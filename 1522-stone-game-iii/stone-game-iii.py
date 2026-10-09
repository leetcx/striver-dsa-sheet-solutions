class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        z=len(stoneValue)
        dp={}
        def check(person,i):
            if i>=z:
                return 0
            result=float('-inf')
            state=(person,i)
            if state in dp:
                return dp[state]
            stone=0
            for x in range(1,min(3,z-i)+1):
                stone+=stoneValue[i+x-1]
                
                result=max(result,stone-check(1,i+x))
            dp[state]= result
            return dp[state]
            
                
        m=check(1,0)
        if m==0:
            return "Tie"
        elif m>0:
            return "Alice"
        else:
            return "Bob"

                