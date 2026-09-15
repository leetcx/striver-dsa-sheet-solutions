class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans=[]
        odd=[]
        low=0
        high=len(nums)-1
        
        while low<=high:
            if nums[low]%2==0:
                ans.append(nums[low])
                
            else:
                odd.append(nums[low])
            low+=1
        nums[:]=ans+odd

        return nums

