class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        temp = []

        for i in range(1, m + 1):
            temp.append(i)

        MOD = 10**9 + 7

        dp = [[[-1] * (k + 1) for _ in range(m + 1)]
              for _ in range(n + 1)]

        def arrays(i, length, maxval, searchcost):

            if length == n:
                return 1 if searchcost == k else 0

            if searchcost > k:
                return 0

            if i >= len(temp):
                return 0

            if dp[length][maxval][searchcost] != -1:
                return dp[length][maxval][searchcost]

            # TAKE
            if temp[i] > maxval:
                take = arrays(
                    0,
                    length + 1,
                    temp[i],
                    searchcost + 1
                )
            else:
                take = arrays(
                    0,
                    length + 1,
                    maxval,
                    searchcost
                )

            # SKIP
            skip = arrays(
                i + 1,
                length,
                maxval,
                searchcost
            )

            dp[length][maxval][searchcost] = (take + skip) % MOD

            return dp[length][maxval][searchcost]

        return arrays(0, 0, 0, 0) % MOD