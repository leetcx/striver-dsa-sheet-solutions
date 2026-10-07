class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        MOD = 10**9 + 7

        # suffix[i][j] = number of apples in rectangle
        # from (i,j) to bottom-right
        suffix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                suffix[i][j] = (
                    (pizza[i][j] == "A")
                    + suffix[i + 1][j]
                    + suffix[i][j + 1]
                    - suffix[i + 1][j + 1]
                )

        def hasapple(i, j, r, c):
            return (
                suffix[i][j]
                - suffix[r][j]
                - suffix[i][c]
                + suffix[r][c]
            ) > 0

        dp = {}

        def count(i, j, cuts):

            if cuts == k - 1:
                if hasapple(i, j, m, n):
                    return 1
                return 0

            state = (i, j, cuts)

            if state in dp:
                return dp[state]

            ways = 0

            # Horizontal cuts
            for r in range(i + 1, m):
                if hasapple(i, j, r, n) and hasapple(r, j, m, n):
                    ways += count(r, j, cuts + 1)

            # Vertical cuts
            for c in range(j + 1, n):
                if hasapple(i, j, m, c) and hasapple(i, c, m, n):
                    ways += count(i, c, cuts + 1)

            dp[state] = ways % MOD
            return dp[state]

        return count(0, 0, 0)