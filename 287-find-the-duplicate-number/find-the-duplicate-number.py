class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        set1={}
        for i in nums:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for p in range(len(set1)):
            if set1[nums[p]]>1:
                return nums[p]
        return 0