class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while mid<=high:
            if nums[mid]%2==0:
                temp=nums[mid]
                nums[mid]=nums[low]
                nums[low]=temp
                low+=1
                mid+=1
            else:
                temp=nums[mid]
                nums[mid]=nums[high]
                nums[high]=temp
                high-=1
        return nums
