class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        z = len(words[0])
        p = len(target)
        MOD = 10**9 + 7

        count = [[0] * 26 for _ in range(z)]

        for i in range(z):
            for word in words:
                count[i][ord(word[i]) - ord('a')] += 1

        dp = {}

        def check(i, j):
            if j == p:
                return 1

            if i >= z:
                return 0

            state = (i, j)
            if state in dp:
                return dp[state]

            skip = check(i + 1, j)

            take = count[i][ord(target[j]) - ord('a')] * check(i + 1, j + 1)

            dp[state] = (skip + take) % MOD
            return dp[state]

        return check(0, 0)