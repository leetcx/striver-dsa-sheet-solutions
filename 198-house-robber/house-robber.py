class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1]* 2 for _ in range(n)]
        def prof(i,free):
            if i==n:
                return 0
            if dp[i][free] != -1:
                return dp[i][free]
            if free==1:
                c1=nums[i] + prof(i+1,free-1)
                c=prof(i+1,free)
                p=max(c,c1)
                dp[i][free]=p
            else:
           
            
                dp[i][free]=prof(i+1,free+1)

            return dp[i][free]
        return prof(0,1)