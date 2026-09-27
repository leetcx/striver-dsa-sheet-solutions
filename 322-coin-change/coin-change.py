class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount==0:
            return 0
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        def fewest_coins_need(i,calculated_total,moves):
            nonlocal memo
            
            if calculated_total>amount:
                return float('inf')
            if i>=len(coins):
                return float('inf')
            if calculated_total==amount:
                return 0
            if memo[i][calculated_total] != -1:
                return memo[i][calculated_total]
            take=1+fewest_coins_need(i,calculated_total+coins[i],moves)
            
            skip=fewest_coins_need(i+1,calculated_total,moves)
            memo[i][calculated_total]=min(take,skip)
            return memo[i][calculated_total]
        ans= fewest_coins_need(0,0,0)
        if ans==float('inf'):
            return -1
        return ans
        
