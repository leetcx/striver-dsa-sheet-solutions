class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * n for _ in range(n)] for _ in range(m)]

        for row in range(m-1, -1, -1):
            for col1 in range(n):
                for col2 in range(n):

                    if row == m-1:
                        if col1 == col2:
                            dp[row][col1][col2] = grid[row][col1]
                        else:
                            dp[row][col1][col2] = grid[row][col1] + grid[row][col2]
                        continue

                    if col1 == col2:
                        take1 = grid[row][col1] + (dp[row+1][col1-1][col2-1] if col1 > 0 and col2 > 0 else float('-inf'))
                        take2 = grid[row][col1] + (dp[row+1][col1-1][col2] if col1 > 0 else float('-inf'))
                        take3 = grid[row][col1] + (dp[row+1][col1-1][col2+1] if col1 > 0 and col2 < n-1 else float('-inf'))
                        take4 = grid[row][col1] + (dp[row+1][col1][col2-1] if col2 > 0 else float('-inf'))
                        take5 = grid[row][col1] + dp[row+1][col1][col2]
                        take6 = grid[row][col1] + (dp[row+1][col1+1][col2] if col1 < n-1 else float('-inf'))
                        take7 = grid[row][col1] + (dp[row+1][col1][col2+1] if col2 < n-1 else float('-inf'))
                        take8 = grid[row][col1] + (dp[row+1][col1+1][col2+1] if col1 < n-1 and col2 < n-1 else float('-inf'))
                        take9 = grid[row][col1] + (dp[row+1][col1+1][col2-1] if col1 < n-1 and col2 > 0 else float('-inf'))
                    else:
                        take1 = grid[row][col1] + grid[row][col2] + (dp[row+1][col1-1][col2-1] if col1 > 0 and col2 > 0 else float('-inf'))
                        take2 = grid[row][col1] + grid[row][col2] + (dp[row+1][col1-1][col2] if col1 > 0 else float('-inf'))
                        take3 = grid[row][col1] + grid[row][col2] + (dp[row+1][col1-1][col2+1] if col1 > 0 and col2 < n-1 else float('-inf'))
                        take4 = grid[row][col1] + grid[row][col2] + (dp[row+1][col1][col2-1] if col2 > 0 else float('-inf'))
                        take5 = grid[row][col1] + grid[row][col2] + dp[row+1][col1][col2]
                        take6 = grid[row][col1] + grid[row][col2] + (dp[row+1][col1+1][col2] if col1 < n-1 else float('-inf'))
                        take7 = grid[row][col1] + grid[row][col2] + (dp[row+1][col1][col2+1] if col2 < n-1 else float('-inf'))
                        take8 = grid[row][col1] + grid[row][col2] + (dp[row+1][col1+1][col2+1] if col1 < n-1 and col2 < n-1 else float('-inf'))
                        take9 = grid[row][col1] + grid[row][col2] + (dp[row+1][col1+1][col2-1] if col1 < n-1 and col2 > 0 else float('-inf'))

                    dp[row][col1][col2] = max(take1, take2, take3, take4, take5, take6, take7, take8, take9)

        return dp[0][0][n-1]