class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        dp = [[0] * (n + 1) for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):

                if prev == -1:
                    buy = dp[i + 1][i + 1]
                    notbuy = dp[i + 1][0]

                    dp[i][0] = max(buy, notbuy)

                else:
                    sell = prices[i] - prices[prev] + dp[i + 2][0]
                    notsell = dp[i + 1][prev + 1]

                    dp[i][prev + 1] = max(sell, notsell)

        return dp[0][0]