class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
       
       
        lastinvalid = -1
        minindex = -1
        maxindex = -1
        count = 0

        for high in range(len(nums)):

            # Current element cannot be part of a valid subarray
            if nums[high] < mink or nums[high] > maxk:
                lastinvalid = high

            # Latest occurrence of mink
            if nums[high] == mink:
                minindex = high

            # Latest occurrence of maxk
            if nums[high] == maxk:
                maxindex = high

            # Both bounds have been seen
            if minindex != -1 and maxindex != -1:
                earlier = min(minindex, maxindex)
                if earlier > lastinvalid:
                    count += earlier - lastinvalid
                # Number of valid starting positions
                

        return count