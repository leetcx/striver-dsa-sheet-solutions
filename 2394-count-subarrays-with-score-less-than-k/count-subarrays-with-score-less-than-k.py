class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        sum1=0
        count=0
        for high in range(len(nums)):
            sum1+=nums[high]
            score=sum1 *(high-low+1)
            while score>=k:
                sum1-=nums[low]
                
                low+=1
                score=sum1*(high-low+1)
            count+=high-low+1
        return count
        