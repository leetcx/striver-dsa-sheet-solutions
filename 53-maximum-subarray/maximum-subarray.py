class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        maxsum=nums[0]

        for i in range(n):
            sum+=nums[i]
            if sum>maxsum:
                maxsum=sum
            if sum<0:
                sum=0
        return maxsum
