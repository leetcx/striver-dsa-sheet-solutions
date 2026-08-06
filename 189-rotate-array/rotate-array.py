class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        set1=[]
        set2=[]

        k=k%n
        if k==0:
            return nums
        for i in range(n-k,n):
            set1.append(nums[i])
        
        for i in range(n-k):
            set2.append(nums[i])
        nums[::]=set1+set2
        

        