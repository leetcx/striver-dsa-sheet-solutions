class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        low=0
        high=len(nums)-1
        
        while low<=high:
            if nums[low]%2==1 and nums[high]%2==0:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1
                high-=1
            else:
                if nums[low]%2==0 and nums[high]%2==0:
                    low+=1
                else:
                    high-=1

               
            
        
        return nums

