class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        dp={}
        def mini(i,op1av,op2av):
            if i>=len(nums):
                return 0
            state=(i,op1av,op2av)
            if state in dp:
                return dp[state]
            take=float('inf')
            op1do=float('inf')
            op2do=float('inf')
            both=float('inf')
            bothii=float('inf')
            take=nums[i]+mini(i+1,op1av,op2av)
            if op1av>0:
                op1do=((nums[i]+1)//2) +mini(i+1,op1av-1,op2av)
            if nums[i]>=k and op2av>0:
                op2do=(nums[i]-k) + mini(i+1,op1av,op2av-1)
            if op1av>0 and ((nums[i]+1)//2) >=k and op2av>0:
                both= (((nums[i]+1)//2)-k) + mini(i+1,op1av-1,op2av-1)
            if nums[i]>=k and op1av>0 and op2av>0:
                bothii= (((nums[i]-k)+1)//2) + mini(i+1,op1av-1,op2av-1)
            dp[state]= min(take,op1do,op2do,both,bothii)
            return dp[state]
        return mini(0,op1,op2)