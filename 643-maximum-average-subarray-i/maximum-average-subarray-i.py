class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low=0
        high=k-1
        p=sum(nums[low:high+1])
        avg=p/(high-low+1)
        res=float('-inf')
        while high<len(nums):
            res=max(res,avg)
            
            p=p-nums[low]
            
            low+=1
            high+=1
            if high>=len(nums):
                break
            p+=nums[high]
            avg=p/(high-low+1)
        return res
        
