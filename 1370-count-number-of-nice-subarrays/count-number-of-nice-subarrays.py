class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        low=0
        mid=0
        odd=0
        res=0
        for high in range(len(nums)):
            if nums[high] %2==1:
                odd+=1
            while odd>k:
                if nums[low]%2==1:
                    odd-=1
                low+=1
                mid=low
            if odd==k:
                while nums[mid] %2 !=1:
                    mid+=1
                res+=(mid-low)+1
        return res
