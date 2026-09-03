class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        p=max(nums)
        low=0
        count=0
        t=0
        for high in range(len(nums)):
            if nums[high]==p:
                count+=1
            while count >=k and low<=high:
                t+=len(nums)-high
                if nums[low]==p:
                    count-=1
                low+=1
        return t
