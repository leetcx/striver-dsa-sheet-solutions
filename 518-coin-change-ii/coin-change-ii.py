class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp={}
        def ways(i,amount):
            if amount==0:
                return 1
            if i>=len(coins) or amount<0:
                return 0
            state=(i,amount)
            if state in dp:
                return dp[state]
            take=0
            skip=0
            if amount>=coins[i]:
                take+=ways(i,amount-coins[i])
            skip+=ways(i+1,amount)
            dp[state]= take+skip
            return dp[state]
        return ways(0,amount)


