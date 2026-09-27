class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        def target(i,cal):
            nonlocal memo
            if cal>amount:
                return 0
            if i>=len(coins):
                return 0
            
            if cal==amount:
                return 1
            if memo[i][cal] != -1:
                return memo[i][cal]
            take=target(i,cal+coins[i])
            skip=target(i+1,cal)
            memo[i][cal]=take+skip
            return memo[i][cal]
        return target(0,0)
        

            