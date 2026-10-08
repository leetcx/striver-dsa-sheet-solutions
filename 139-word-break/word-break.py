class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp={}
        def convert(i, s, p):
            if i == len(s):
                return True

            if p >= len(wordDict):
                return False
            state=(i,s,p)
            if state in dp:
                return dp[state]
            check1 = False

            if s[i:i+len(wordDict[p])] == wordDict[p]:
                check1 = convert(i + len(wordDict[p]), s, 0)

            check2 = convert(i, s, p + 1)

            dp[state]= check1 or check2
            return dp[state]

        return convert(0, s, 0)
                