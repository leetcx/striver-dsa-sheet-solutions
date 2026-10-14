class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp={}
        def check(i):
            if i>=len(s):
                return 0
            if i in dp:
                return dp[i]
            take = float('inf')
            for j in range(len(dictionary)):
                substr = s[i:i + len(dictionary[j])]
                if substr == dictionary[j]:
                    take = min(take, check(i + len(dictionary[j])))

            skip = 1 + check(i + 1)
            dp[i]= min(take, skip)
            return dp[i]
        return check(0)