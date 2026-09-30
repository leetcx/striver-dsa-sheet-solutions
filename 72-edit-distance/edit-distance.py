class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def solve(i, j):

            if i == m:
                return n - j

            if j == n:
                return m - i

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = solve(i + 1, j + 1)

            else:
                insert = solve(i, j + 1)
                delete = solve(i + 1, j)
                replace = solve(i + 1, j + 1)

                dp[i][j] = 1 + min(insert, delete, replace)

            return dp[i][j]

        return solve(0, 0)