class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n
        prev=1
        prevprev=0
        res=0
        for i in range(2,n+1):
            res=prev+prevprev 
            prevprev=prev
            prev=res
        return res