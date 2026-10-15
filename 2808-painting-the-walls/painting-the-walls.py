class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def mini(i, remaining):
            if remaining <= 0:
                return 0
            if i >= n:
                return float('inf')

            if dp[i][remaining] != -1:
                return dp[i][remaining]

            paid = cost[i] + mini(i + 1, remaining - 1 - time[i])
            skip = mini(i + 1, remaining)

            dp[i][remaining] = min(paid, skip)
            return dp[i][remaining]

        return mini(0, n)