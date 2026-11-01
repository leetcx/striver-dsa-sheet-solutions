class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        result = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 1:
                    right = 1 + dp[i][j + 1]
                    down = 1 + dp[i + 1][j]
                    diag = 1 + dp[i + 1][j + 1]

                    dp[i][j] = min(right, down, diag)
                    result += dp[i][j]

        return result