class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m = len(points)
        n = len(points[0])

        dp = [[-1] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = points[0][i]

        for i in range(1, m):

            left = [0] * n
            right = [0] * n

            left[0] = dp[i-1][0]

            for j in range(1, n):
                left[j] = max(left[j-1] - 1, dp[i-1][j])

            right[n-1] = dp[i-1][n-1]

            for j in range(n-2, -1, -1):
                right[j] = max(right[j+1] - 1, dp[i-1][j])

            for j in range(n):
                dp[i][j] = points[i][j] + max(left[j], right[j])

        return max(dp[m-1])