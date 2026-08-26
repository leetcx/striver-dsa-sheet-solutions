class Solution:
    def climbStairs(self, n: int) -> int:
        ans=1
        next1=1
        next2=1
        for i in range(n-2,-1,-1):
           
            if i==n:
                return 1
            ans=next1+next2
            next2=next1
            next1=ans
        return ans
            
