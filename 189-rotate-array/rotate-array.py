class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        ans=[]
        p=[]
        k=k%n
        if k==0:
            return nums
        for i in range(n-k):
            ans.append(nums[i])
        for i in range(n-k,n):
            p.append(nums[i])
        nums[::]=p+ans