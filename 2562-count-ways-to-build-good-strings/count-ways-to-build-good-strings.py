class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp=[0] * (high+1)
        for i in range(high,-1,-1):
            
            
            take=0
            take1=0
            if i+zero<=high:
                take=dp[i+zero]
            if i+one<=high:
                take1=dp[i+one]
            
            if low <= i <= high:
                dp[i] = 1 + take + take1
            else:
                dp[i] = take + take1
        return dp[0] % ((10**9)+7)