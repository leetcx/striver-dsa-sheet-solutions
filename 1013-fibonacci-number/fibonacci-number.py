class Solution:
    def fib(self, n: int) -> int:
        def fib(n):
            if n==1 or n==0:
                return n
            a=fib(n-1)
            b=fib(n-2)
            total=a+b
            return total
        return fib(n)