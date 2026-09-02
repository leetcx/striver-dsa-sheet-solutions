class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=len(nums)-1
            while low<high:
                sum1=nums[i]+nums[low]+nums[high]
                if sum1==0:
                    ans.append((nums[i],nums[low],nums[high]))
                    low+=1
                    high-=1
                    while low<high and nums[low]==nums[low-1]:
                        low+=1
                    while low<high and nums[high]==nums[high+1]:
                        high-=1
                else:
                    if sum1>0:
                        high-=1
                    else:
                        low+=1
        return ans