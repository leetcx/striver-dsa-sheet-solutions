class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def valid(i, open, close):
            
            if open<close:
                return False
            if i >= len(s):
                return open == close

            state = (i, open, close)
            if state in dp:
                return dp[state]

            if s[i] == "*":
                dp[state] = (
                    valid(i + 1, open, close) or
                    valid(i + 1, open + 1, close) or
                    valid(i + 1,open, close + 1)
                )
            elif s[i] == "(":
                dp[state] = valid(i + 1, open + 1, close)
            elif s[i] == ")":
                dp[state] = valid(i + 1, open, close + 1)

            return dp[state]

        return valid(0, 0, 0)
