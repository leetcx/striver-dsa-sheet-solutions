class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        low=0
        high=0
        cost=0
        res=float('-inf')
        sum1=0
        for high in range(len(nums)):
            sum1+=nums[high]
            cost=nums[high] *(high-low+1) -sum1
            while cost>k and low<high:
                sum1-=nums[low]
                
                low+=1
                cost=nums[high] *(high-low+1) - sum1
                
            res=max(res,high-low+1)
        return res