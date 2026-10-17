class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = ""
        maxlen = 0

        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1

                if s[i] == s[j]:
                    if l <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if l > maxlen:
                            ans = s[i:j + 1]
                            maxlen = l

        return ans     
