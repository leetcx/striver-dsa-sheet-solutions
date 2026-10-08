class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        dp = [-1] * (len(s) + 1)

        def build(i):
            if i == len(s):
                return 1

            if dp[i] != -1:
                return dp[i]

            if s[i] == "0":
                return 0

            take = 0
            num = 0

            for j in range(i, len(s)):
                num = num * 10 + int(s[j])

                if num > k:
                    break

                take += build(j + 1)
                take %= MOD

            dp[i] = take
            return take

        return build(0)