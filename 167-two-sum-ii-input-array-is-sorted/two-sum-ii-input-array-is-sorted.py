class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        ans=[] 
        while low<high:
            sum1=nums[low]+nums[high]
            if sum1==target:
                ans.append(low+1)
                ans.append(high+1)
                break
            else:
                if sum1>target:
                    high-=1
                else:
                    low+=1
        return ans
