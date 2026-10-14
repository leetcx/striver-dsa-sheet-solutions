class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {}

        def check(i, j):
            if i >= len(s):
                return 0

            if j >= len(dictionary):
                return 1 + check(i + 1, 0)

            state = (i, j)
            if state in dp:
                return dp[state]

            substr1 = s[i:i + len(dictionary[j])]

            if substr1 == dictionary[j]:
                take = check(i + len(dictionary[j]), 0)
            else:
                take = float('inf')

            skip = check(i, j + 1)

            dp[state] = min(take, skip)
            return dp[state]

        return check(0, 0)