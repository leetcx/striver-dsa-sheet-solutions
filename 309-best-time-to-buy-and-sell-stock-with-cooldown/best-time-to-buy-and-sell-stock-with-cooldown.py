class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0

        dp = [0] * n

        dp[0] = 0
        dp[1] = max(prices[1] - prices[0], 0)

        for i in range(2, n):
            dp[i] = dp[i - 1]

            for j in range(i):
                profittod = prices[i] - prices[j]

                prev = 0
                if j - 2 >= 0:
                    prev = dp[j - 2]

                dp[i] = max(dp[i], profittod + prev)

        return dp[n - 1]