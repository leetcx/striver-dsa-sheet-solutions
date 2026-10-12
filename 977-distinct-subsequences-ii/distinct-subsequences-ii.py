class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * 26
        mod = 10**9 + 7

        for ch in s:
            dp[ord(ch) - ord('a')] = (sum(dp) + 1) % mod

        return sum(dp) % mod