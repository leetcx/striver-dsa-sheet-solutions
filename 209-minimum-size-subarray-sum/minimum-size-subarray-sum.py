class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        sum1=0
        sum1+=nums[0]
        minlen=float('inf')
        while low<=high and high <len(nums):
            if sum1>=target:
                p=high-low+1
                minlen=min(minlen,p)
                low+=1
                if low<=high:
                    sum1-=nums[low-1]
            else:
                high+=1
                if high==len(nums):
                    break
                sum1+=nums[high]
        if minlen == float('inf'):
            return 0
        return minlen
