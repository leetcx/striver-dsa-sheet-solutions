class Solution:
    def numSquares(self, n: int) -> int:
        
        ans=0
        minlen=float('inf')
        memo={}
        def check(rem):
            
            if rem<0:
                return float('inf')
            
            if rem==0:
                return 0
            
            state=rem
            if state in memo:
                return memo[state]
            minres=float('inf')
            for i in range(1, int(n**0.5) + 1):
                take=1+check(rem-(i*i))
                minres=min(take,minres)
            memo[state]=minres
            return memo[state]
        return check(n)