class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def countsteps(i, k):
            clock = abs(i - k)
            anti = abs(len(ring) - clock)
            return min(clock, anti)

        dp = [[-1] * (len(key) + 1) for _ in range(len(ring))]

        for i in range(len(ring)):
            dp[i][len(key)] = 0

        for j in range(len(key) - 1, -1, -1):
            for i in range(len(ring)):
                result = float('inf')

                for k in range(len(ring)):
                    if ring[k] == key[j]:
                        steps = countsteps(i, k)
                        totalsteps = steps + 1 + dp[k][j + 1]
                        result = min(result, totalsteps)

                dp[i][j] = result

        return dp[0][0]