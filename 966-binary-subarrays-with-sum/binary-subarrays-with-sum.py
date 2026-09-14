class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(goal):
            count=0
            low=0
            sum1=0
            for high in range(len(nums)):
                sum1+=nums[high]
                while sum1>goal and low<=high:
                    sum1-=nums[low]
                    low+=1
            
                count+=high-low+1
               
            return count
        return atmost(goal)-atmost(goal-1)
