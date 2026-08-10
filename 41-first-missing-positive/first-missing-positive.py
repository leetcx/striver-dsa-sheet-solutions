class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>(n):
                nums[i]=n+1
        for i in range(n):
            s=abs(nums[i])
            if s<=n:
                p=s-1
                if nums[p]>0:
                    nums[p]=-nums[p]
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1

        
                
        