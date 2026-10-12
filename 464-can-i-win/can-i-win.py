class Solution:
    def canIWin(self, maxChoosableInteger: int, desired: int) -> bool:
        if desired <= 0:
            return True

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total < desired:
            return False

        dp = {}

        def check(used, remaining):
            state = (used, remaining)

            if state in dp:
                return dp[state]

            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)

                if used & bit:
                    continue

                if i >= remaining:
                    dp[state] = True
                    return True

                ans = check(used | bit, remaining - i)

                if not ans:
                    dp[state] = True
                    return True

            dp[state] = False
            return False

        return check(0, desired)