class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        n=len(nums)
        p=float('inf')
        ans=0
        for i in range (n):
            if i>0 and nums[i-1]==nums[i]:
                continue
            left=i+1
            right=n-1
            while left<right:
                sum1=nums[i]+nums[left]+nums[right]
                q=abs(sum1-target)
                if q< p:
                    p=q
                    ans=sum1
                    
                    
                    
                else:
                    if sum1==target:
                        return sum1
                    if sum1>target:

                        right-=1
                    else:
                       
                        left+=1
        return ans


                    
            
