from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq=deque()
        maxq=deque()
        res=float('-inf')
        low=0
        for high in range(len(nums)):
            while minq and nums[minq[-1]] > nums[high]:
                minq.pop()
            minq.append(high)
            while maxq and nums[maxq[-1]] < nums[high]:
                maxq.pop()
            maxq.append(high)
            diff=nums[maxq[0]]-nums[minq[0]]
            while diff> limit:
                if low == minq[0]:
                    minq.popleft()
                if low == maxq[0]:
                    maxq.popleft()
               
                low+=1
                diff=nums[maxq[0]]-nums[minq[0]]
            if diff<=limit:
                lou=high-low+1
                res=max(res,lou)
        return res
