class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float('inf')
        for i in range(len(nums)):
            low=i+1
            high=len(nums)-1
            
            while low<high:
                sum1=nums[i]+nums[low]+nums[high]
                if sum1==target:
                    return sum1
                diff=abs(target-sum1)
                if diff<ans:
                    ans=diff
                    p=sum1
                if sum1>target:
                    high-=1
                else:
                    low+=1
        if ans==float('inf'):
            return 0
        return p

