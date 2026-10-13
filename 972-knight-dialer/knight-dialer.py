
class Solution:
    def knightDialer(self, n: int) -> int:
        dialpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
        rows = len(dialpad)
        cols = len(dialpad[0])
        dp = {}

        def doit(i, j, remaining):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            if dialpad[i][j] == -1:
                return 0
            if remaining == 1:
                return 1

            state = (i, j, remaining)
            if state in dp:
                return dp[state]

            moves = 0
            moves += doit(i-1, j-2, remaining-1)
            moves += doit(i-2, j-1, remaining-1)
            moves += doit(i-2, j+1, remaining-1)
            moves += doit(i-1, j+2, remaining-1)
            moves += doit(i+1, j-2, remaining-1)
            moves += doit(i+2, j-1, remaining-1)
            moves += doit(i+2, j+1, remaining-1)
            moves += doit(i+1, j+2, remaining-1)

            dp[state] = moves % (10**9 + 7)
            return dp[state]

        ans = 0
        for p in range(rows):
            for q in range(cols):
                if dialpad[p][q] != -1:
                    ans += doit(p, q, n)

        return ans % (10**9 + 7)
