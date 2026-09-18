class Solution:
    def numSubarraysWithSum(self, nums: list[int], k: int) -> int:
        def atmost(k):
            sum1=0
            low=0
            count=0
            for high in range(len(nums)):
                sum1+=nums[high]
                while sum1>k and low<=high:
                    sum1-=nums[low]
                    low+=1
                count+=high-low+1
            return count
        return atmost(k)-atmost(k-1)
