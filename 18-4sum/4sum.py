class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l=len(nums)
        ans=[]
        for i in range(l-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,l-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                low=j+1
                high=l-1

                while low<high:
                    sum=nums[i]+nums[j]+nums[low]+nums[high]
                    if sum==target:
                        ans.append((nums[i],nums[j],nums[low],nums[high]))
                        low+=1
                        high-=1
                    
                        while low<high and nums[low]==nums[low-1]:
                            low+=1
                            
                        while low<high and nums[high]==nums[high+1]:
                            high-=1
                            

                        
                        
                    elif sum>target:
                        high-=1
                    elif sum<target:
                        low+=1
        return ans
                

