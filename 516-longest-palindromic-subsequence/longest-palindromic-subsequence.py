class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):

            if i > j:
                return 0

            if i == j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = 2 + solve(i + 1, j - 1)

            else:
                dp[i][j] = max(
                    solve(i + 1, j),
                    solve(i, j - 1)
                )

            return dp[i][j]

        return solve(0, n - 1)