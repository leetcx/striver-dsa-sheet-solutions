class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        c=1
        ans=[]
        for i in range(1,n):
            if nums[i-1]==nums[i]:
                c+=1
            else:
                c=1
            if c>n//3 and nums[i-1] not in ans:
                ans.append(nums[i-1])
        if c>n//3 and nums[n-1] not in ans:
            ans.append(nums[n-1])
        return ans