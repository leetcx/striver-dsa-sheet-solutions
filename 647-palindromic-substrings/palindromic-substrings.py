class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def palin(i, j):

            if i >= j:
                return True

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] != s[j]:
                dp[i][j] = False
            else:
                dp[i][j] = palin(i + 1, j - 1)

            return dp[i][j]

        ans = 0

        for i in range(n):
            for j in range(i, n):
                if palin(i, j):
                    ans += 1

        return ans