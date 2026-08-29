class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low=0
        high=len(nums)-1
        n=len(nums)
        ans=[0] * n
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[low]) > abs(nums[high]):
                ans[i]=nums[low] **2
                low+=1
            else:
                ans[i] = nums[high] **2
                high-=1
                
        return ans