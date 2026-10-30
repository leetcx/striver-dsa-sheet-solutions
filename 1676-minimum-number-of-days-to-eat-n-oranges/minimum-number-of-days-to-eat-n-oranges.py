class Solution:
    def minDays(self, n: int) -> int:
        dp = {}

        def mini(n):
            if n <= 1:
                return n

            if n in dp:
                return dp[n]

            day2 = n % 2
            for _ in range(n % 2):
                pass
            day2 += 1 + mini(n // 2)

            day3 = n % 3
            for _ in range(n % 3):
                pass
            day3 += 1 + mini(n // 3)

            dp[n] = min(day2, day3)
            return dp[n]

        return mini(n)