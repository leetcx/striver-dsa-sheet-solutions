
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = {}

        def cal(countsong, countunique):
            if countsong == goal:
                if countunique == n:
                    return 1
                return 0

            state = (countsong, countunique)
            if state in dp:
                return dp[state]

            take = 0

            take += (n - countunique) * cal(countsong + 1, countunique + 1)

            if countunique > k:
                take += (countunique - k) * cal(countsong + 1, countunique)

            dp[state] = take
            return dp[state] % ((10**9)+7)

        return cal(0, 0) % ((10**9)+7)
