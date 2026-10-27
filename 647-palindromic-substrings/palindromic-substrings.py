class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1

                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    count += 1

        return count