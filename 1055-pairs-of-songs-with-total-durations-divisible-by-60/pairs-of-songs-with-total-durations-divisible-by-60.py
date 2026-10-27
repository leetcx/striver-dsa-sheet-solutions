class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        dp = {}
        count = 0

        for j in time:
            target = (60 - j % 60) % 60
            count += dp.get(target, 0)

            r = j % 60
            dp[r] = dp.get(r, 0) + 1

        return count