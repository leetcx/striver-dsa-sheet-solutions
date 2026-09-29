class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        MOD = 10**9 + 7

        dp = [
            [[0] * (k + 1) for _ in range(m + 1)]
            for _ in range(n + 1)
        ]

        dp[0][0][0] = 1

        for length in range(n):

            for maxval in range(m + 1):

                for searchcost in range(k + 1):

                    curr = dp[length][maxval][searchcost]

                    if curr == 0:
                        continue

                    # Choose a value <= current maximum
                    if maxval > 0:
                        dp[length + 1][maxval][searchcost] += (
                            curr * maxval
                        ) % MOD

                        dp[length + 1][maxval][searchcost] %= MOD

                    # Choose a new maximum
                    if searchcost < k:

                        for x in range(maxval + 1, m + 1):
                            dp[length + 1][x][searchcost + 1] += curr
                            dp[length + 1][x][searchcost + 1] %= MOD

        ans = 0

        for maxval in range(1, m + 1):
            ans += dp[n][maxval][k]

        return ans % MOD