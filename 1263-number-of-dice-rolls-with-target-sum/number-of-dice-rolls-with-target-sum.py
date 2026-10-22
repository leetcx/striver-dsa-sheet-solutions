class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(target+1):
            
                ways=0
                for k in range(1,k+1):
                    if j-k>=0:
                        ways+=dp[i-1][j-k]
                dp[i][j]= ways % ((10**9+7))
            
        return dp[n][target]
            