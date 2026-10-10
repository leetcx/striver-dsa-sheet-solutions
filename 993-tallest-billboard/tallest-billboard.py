class Solution:
    def tallestBillboard(self, rod: list[int]) -> int:
        dp={}
        def maximum(i,d):
            if i>=len(rod):
                if d==0:
                    return 0
                return float('-inf')
            state=(i,d)
            if state in dp:
                return dp[state]
            take1=maximum(i+1,d+rod[i])
            take2=rod[i]+maximum(i+1,d-rod[i])
            skip1=maximum(i+1,d)
            dp[state]=max(take1,take2,skip1)
            return dp[state]
        return maximum(0,0)