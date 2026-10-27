class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        n = len(time)
        dp = [[[0] * 3 for _ in range(60)] for _ in range(n + 1)]

        for i in range(60):
            dp[n][i][2] = 1 if i == 0 else 0

        for j in range(n - 1, -1, -1):
            for i in range(60):
                for p in range(2, -1, -1):
                    if p == 2:
                        dp[j][i][p] = 1 if i == 0 else 0
                    else:
                        take = dp[j + 1][(i + time[j]) % 60][p + 1]
                        skip = dp[j + 1][i][p]
                        dp[j][i][p] = take + skip

        return dp[0][0][0]