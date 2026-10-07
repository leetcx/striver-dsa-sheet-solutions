class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        z = len(words[0])
        p = len(target)
        MOD = 10**9 + 7

        dp = [[0] * (p + 1) for _ in range(z + 1)]
        dp[z][p] = 1

        # count[i][c] = how many words have character c at column i
        count = [[0] * 26 for _ in range(z)]

        for i in range(z):
            for word in words:
                count[i][ord(word[i]) - ord('a')] += 1

        for i in range(z - 1, -1, -1):
            for j in range(p, -1, -1):

                if j == len(target):
                    dp[i][j] = 1
                    continue

                skip = dp[i + 1][j]

                take = count[i][ord(target[j]) - ord('a')] * dp[i + 1][j + 1]

                dp[i][j] = (take + skip) % MOD

        return dp[0][0]