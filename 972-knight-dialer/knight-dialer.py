class Solution:
    def knightDialer(self, n: int) -> int:
        adj = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        mod = 10**9 + 7
        dp = [[0] * 10 for _ in range(n)]

        for i in range(10):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(10):
                for k in adj[j]:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % mod

        ans = 0
        for i in range(10):
            ans = (ans + dp[n-1][i]) % mod

        return ans
        