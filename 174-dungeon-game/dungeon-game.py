class Solution:
    def calculateMinimumHP(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        low = 1
        high = 0

        for i in range(m):
            for j in range(n):
                high += abs(grid[i][j])

        high += 1

        while low < high:

            mid = (low + high) // 2

            dp = [[-1] * n for _ in range(m)]

            start = mid + grid[0][0]

            if start <= 0:
                possible = False
            else:
                dp[0][0] = start

                for i in range(m):
                    for j in range(n):

                        if dp[i][j] <= 0:
                            continue

                        if i + 1 < m:
                            health = dp[i][j] + grid[i + 1][j]

                            if health > 0:
                                dp[i + 1][j] = max(
                                    dp[i + 1][j],
                                    health
                                )

                        if j + 1 < n:
                            health = dp[i][j] + grid[i][j + 1]

                            if health > 0:
                                dp[i][j + 1] = max(
                                    dp[i][j + 1],
                                    health
                                )

                possible = dp[m - 1][n - 1] > 0

            if possible:
                high = mid
            else:
                low = mid + 1

        return low