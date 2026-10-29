class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[[-1] * n for _ in range(3)] for _ in range(2)]

        def ways(a, l, lenu):
            if lenu == n:
                return 1

            if dp[a][l][lenu] != -1:
                return dp[a][l][lenu]

            latedays = 0
            absent = 0
            present = 0

            if l < 2:
                latedays += ways(a, l + 1, lenu + 1)

            if a == 0:
                absent += ways(a + 1, 0, lenu + 1)

            present += ways(a, 0, lenu + 1)

            dp[a][l][lenu] = (latedays + absent + present) % mod
            return dp[a][l][lenu]

        return ways(0, 0, 0)