class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        temp=[]
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            temp.append(sum1)
        return temp