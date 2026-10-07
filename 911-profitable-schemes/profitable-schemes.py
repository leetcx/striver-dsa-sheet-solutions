class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        dp={}
        def count(i,profits,nofpep):
            if nofpep>n:
                return 0
            if profits > minProfit:
                profits = minProfit
            if i >=len(group):
                if profits>=minProfit and nofpep<=n:
                    return 1
                return 0
            state=(i,profits,nofpep)
            if state in dp:
                return dp[state]

            take=0
            nottake=0
            nottake+=count(i+1,profits,nofpep)
            take+=count(i+1,profits+profit[i],nofpep+group[i])
            dp[state]= nottake+take
            return dp[state]
        return count(0,0,0) % ((10**9)+7)
