class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n=len(nums)
        z = len(nums) // 2
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        dp={}
        used=[False] * len(nums)
        def maxscore(l,used ,nums):
            if l > z :
                return 0

            
            state=(tuple(used))
            if state in dp:
                return dp[state]
            res=float('-inf')
            for i in range(n-1):
                if used[i]==True:
                    continue
                for j in range(i+1,n):
                    if used[j]:
                        continue
                    used[i]=True
                    used[j]=True
                    score=l*gcd(nums[i],nums[j]) + maxscore(l+1,used,nums)
                    used[i]=False
                    used[j]=False
                    res=max(res,score)
            dp[state]= res
            return res
        return maxscore(1,used,nums)
            

                
