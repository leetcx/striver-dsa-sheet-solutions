class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        leftp=[1] *len(nums)
        p=1
        for i in range(1,len(nums)):
            p*=nums[i-1]
            leftp[i]=p
        rightp=[1] * len(nums)
        c=1
        
        for i in range(len(nums)-2,-1,-1):
            c*=nums[i+1]
            rightp[i]=c
        d=0
        for i in range(len(nums)):
            nums[d]=leftp[i]*rightp[i]
            d+=1
        return nums
