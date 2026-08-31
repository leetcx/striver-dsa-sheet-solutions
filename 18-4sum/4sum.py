class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                low=j+1
                high=len(nums)-1
                while low<high :
                    sum1=nums[i] +nums[j] +nums[low]+ nums[high]
                    if sum1==target:
                        ans.append((nums[i] ,nums[j] ,nums[low] ,nums[high]))
                        low+=1
                        high-=1
                        while low<high and nums[low]==nums[low-1]:
                            low+=1
                        while low <high and nums[high]==nums[high+1]:
                            high-=1
                    else:
                        if sum1> target:
                            high-=1
                        else:
                            low+=1
        return ans
                        