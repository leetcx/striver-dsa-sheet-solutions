class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[[-1] * (n+1) for _ in range(3)] for _ in range(2)]

        for lenu in range(n,-1,-1):
            for l in range(3-1,-1,-1):
                for a in range(2-1,-1,-1):
               

                    if lenu == n:
                        dp[a][l][lenu]= 1
                        continue

            

                    latedays = 0
                    absent = 0
                    present = 0

                    if l < 2:
                        latedays += dp[a][l + 1][ lenu + 1]

                    if a == 0:
                        absent += dp[a + 1][0][lenu + 1]

                    present += dp[a][0][lenu + 1]
                    dp[a][l][lenu] = (latedays + absent + present) % mod

            

        return dp[0][0][0]