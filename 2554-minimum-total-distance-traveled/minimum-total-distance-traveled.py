class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()

        dp = {}

        def mini(i, j):
            if i == len(robot):
                return 0

            if j == len(factory):
                return float('inf')

            state = (i, j)
            if state in dp:
                return dp[state]

            ans = mini(i, j + 1)

            total = 0

            for k in range(factory[j][1]):
                if i + k >= len(robot):
                    break

                total += abs(robot[i + k] - factory[j][0])

                score = total + mini(i + k + 1, j + 1)
                ans = min(ans, score)

            dp[state] = ans
            return dp[state]

        return mini(0, 0)