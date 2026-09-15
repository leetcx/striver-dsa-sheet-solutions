class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        res=float('inf')
        for i in range(len(nums)):
            low=i+1
            high=len(nums)-1
            while low<high:
                sum1=nums[i]+nums[low]+nums[high]
                if sum1==target:
                    return sum1
                diff=abs(sum1-target)
                if diff< res:
                    ans=sum1
                    res=diff
                if sum1>target:
                    high-=1
                else:
                    low+=1


        return ans
