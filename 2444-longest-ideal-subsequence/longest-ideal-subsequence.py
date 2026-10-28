class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for ch in s:
            curr = ord(ch) - ord('a')
            best = 0

            for j in range(max(0, curr - k), min(25, curr + k) + 1):
                best = max(best, dp[j])

            dp[curr] = best + 1

        return max(dp)