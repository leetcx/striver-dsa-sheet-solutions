class Solution:
    def fib(self, n: int) -> int:
        dp={}
        def print(n):
            nonlocal dp
            if n==0 or n==1:
                return n
            if n in dp:
                return dp.get(n)
            a=print(n-1)
            b=print(n-2)
            ans=a+b
            dp[n]=ans
            return ans
        return print(n)
            
        
