class Solution:
    def canCross(self, stones: list[int]) -> bool:
        if len(stones) < 2 or stones[1] != 1:
            return False

        dp = {}

        def check(i, k):
            if i == len(stones) - 1:
                return True
            if k <= 0:
                return False

            state = (i, k)
            if state in dp:
                return dp[state]

            p = False
            z = False
            m = False

            destination = stones[i] + k + 1

            if destination in stones:
                nextind = stones.index(destination)
                p = check(nextind, k + 1)

            if k - 1 > 0:
                destination = stones[i] + (k - 1)

                if destination in stones:
                    nextind = stones.index(destination)
                    z = check(nextind, k - 1)

            destination = stones[i] + k

            if destination in stones:
                nextind = stones.index(destination)
                m = check(nextind, k)

            dp[state] = p or z or m
            return dp[state]

        return check(1, 1)