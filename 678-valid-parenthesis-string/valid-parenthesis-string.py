class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def valid(i, open):
            
            if open<0:
                return False
            if i >= len(s):
                return open == 0

            state = (i, open)
            if state in dp:
                return dp[state]

            if s[i] == "*":
                dp[state] = (
                    valid(i + 1, open) or
                    valid(i + 1, open + 1) or
                    valid(i + 1,open-1)
                )
            elif s[i] == "(":
                dp[state] = valid(i + 1, open + 1)
            elif s[i] == ")":
                dp[state] = valid(i + 1, open-1)

            return dp[state]

        return valid(0, 0)
