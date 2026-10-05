class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2 or n==0:
            return n
        
        a=1
        b=2
        c=3
        for i in range(3,n+1):
           c=a+b
           temp=b
           b=c
           a=temp
            
            

        return c