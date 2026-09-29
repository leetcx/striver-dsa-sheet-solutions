class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        maxlis=float('-inf')
        t=[1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    t[i]=max(t[i],t[j]+1)
                    maxlis=max(t[i],maxlis)
        if maxlis==float('-inf'):
            return 1
        return maxlis