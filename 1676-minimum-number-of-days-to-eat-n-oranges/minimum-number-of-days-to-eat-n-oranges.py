class Solution:
    def minDays(self, n: int) -> int:
        dp = {}

        def mini(n):
            if n <=1:
                return n

            if n in dp:
                return dp[n]

            day1 = n % 2 + 1 + mini(n // 2)
            day2 = n % 3 + 1 + mini(n // 3)

            dp[n] = min(day1, day2)
            return dp[n]

        return mini(n)