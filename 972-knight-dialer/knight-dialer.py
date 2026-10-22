class Solution:
    def knightDialer(self, n: int) -> int:
        p = [[0] * 3 for _ in range(4)]
        c = 1
        for i in range(4):
            for j in range(3):
                if i == 3 and j == 0:
                    p[i][j] = "*"
                    continue
                if i == 3 and j == 2:
                    p[i][j] = "#"
                    continue
                if i == 3 and j == 1:
                    p[i][j] = 0
                    continue
                p[i][j] = c
                c += 1

        mod = 10**9 + 7
        dp = [[[0] * n for _ in range(3)] for _ in range(4)]

        for i in range(4):
            for j in range(3):
                if p[i][j] == "*" or p[i][j] == "#":
                    continue
                dp[i][j][0] = 1

        for k in range(1, n):
            for i in range(4):
                for j in range(3):
                    if p[i][j] == "*" or p[i][j] == "#":
                        continue

                    dp[i][j][k] = (
                        (dp[i-2][j-1][k-1] if i-2 >= 0 and j-1 >= 0 else 0) +
                        (dp[i-2][j+1][k-1] if i-2 >= 0 and j+1 < 3 else 0) +
                        (dp[i-1][j-2][k-1] if i-1 >= 0 and j-2 >= 0 else 0) +
                        (dp[i-1][j+2][k-1] if i-1 >= 0 and j+2 < 3 else 0) +
                        (dp[i+1][j-2][k-1] if i+1 < 4 and j-2 >= 0 else 0) +
                        (dp[i+1][j+2][k-1] if i+1 < 4 and j+2 < 3 else 0) +
                        (dp[i+2][j-1][k-1] if i+2 < 4 and j-1 >= 0 else 0) +
                        (dp[i+2][j+1][k-1] if i+2 < 4 and j+1 < 3 else 0)
                    ) % mod

        ans = 0
        for i in range(4):
            for j in range(3):
                if p[i][j] == "*" or p[i][j] == "#":
                    continue
                ans += dp[i][j][n-1]

        return ans % mod