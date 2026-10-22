class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp={}
        def no(n,target):
            if target==0 and n==0:
                return 1
            if n==0 or target<0:
                return 0
            state=(n,target)
            if state in dp:
                return dp[state]
            ways=0
            for i in range(1,k+1):
                ways+=no(n-1,target-i)
            dp[state]= ways % ((10**9+7))
            return dp[state] % ((10**9+7))
        return no(n,target) % ((10**9+7))
            