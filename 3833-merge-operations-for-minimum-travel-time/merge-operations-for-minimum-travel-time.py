
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        prefix = [0] * (n + 1)

        for x in range(n):
            prefix[x+1] = prefix[x] + time[x]

        dp = {}

        def solve(i, k, last):
            if i == n-1:
                return 0 if k == 0 else float('inf')

            state = (i, k, last)
            if state in dp:
                return dp[state]

            curr = prefix[i+1] - prefix[last]
            ans = float('inf')

            for j in range(i+1, min(n, i+k+2)):
                used = j-i-1

                take = (position[j] - position[i]) * curr
                take += solve(j, k-used, i+1)

                ans = min(ans, take)

            dp[state] = ans
            return ans

        return solve(0, k, 0)
