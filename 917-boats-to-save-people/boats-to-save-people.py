class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        low=0
        high=len(nums)-1
        count=0
        while low<=high:
            sum1=nums[low]+nums[high]
            if sum1>limit:
                boats=sum1//limit
                count+=boats
                high-=1
            else:
                count+=1
                low+=1
                high-=1
        return count
            
