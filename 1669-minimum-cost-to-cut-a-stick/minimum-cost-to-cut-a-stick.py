class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp={}
        def solve(left,right):
            if right-left<2:
                return 0
            state=(left,right)
            if state in dp:
                return dp[state]
            ans=float('inf')
            for i in range(left+1,right):
                cost=cuts[right]-cuts[left]+solve(left,i)  + solve(i,right)
                ans=min(ans,cost)
            dp[state]= ans
            return dp[state]
        return solve(0,len(cuts)-1)
                         