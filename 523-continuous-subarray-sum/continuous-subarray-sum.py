class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        low=0
        high=0
        sum1=0
        set1={0:-1}
        for high in range(len(nums)):
            sum1+=nums[high]
            div=sum1%k
            if div in set1:
                ans=high-set1[div]
                if ans>=2:
                    return True
                
            else:
                set1[div]=high
        return False