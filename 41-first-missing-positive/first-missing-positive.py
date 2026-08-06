class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)

        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=n+1
        for i in range(n):
            n1=abs(nums[i])
            if n1>n:
                continue
            if nums[n1-1]>0 :
                nums[n1-1]=nums[n1-1]*-1
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1
