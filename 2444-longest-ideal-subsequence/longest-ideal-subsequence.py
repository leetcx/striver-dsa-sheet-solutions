class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        result=float('-inf')
        for ch in s:
            curr = ord(ch) - ord('a')
            best = 0

            left=max(0,curr-k)
            right=min(25,curr+k)
            
            for j in range(left,right+1):
                best=max(best,dp[j])
            dp[curr]=max(dp[curr],best+1)
            result=max(result,dp[curr])
        return result