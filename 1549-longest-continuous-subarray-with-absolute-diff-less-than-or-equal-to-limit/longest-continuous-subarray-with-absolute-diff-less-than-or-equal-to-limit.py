from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        low=0
        high=0
        maxq=deque()
        minq=deque()
        res=float('-inf')
        for high in range(len(nums)):
            while maxq and nums[maxq[-1]] < nums[high]:
                maxq.pop()
            maxq.append(high)
           
            while minq and nums[minq[-1]]  > nums[high]:
                minq.pop()          
            minq.append(high)   
            
           
            while nums[maxq[0]] -nums[minq[0]]> limit:
                if minq[0]==low:
                    minq.popleft()
                
                if maxq[0]==low:
                    maxq.popleft()
                low+=1
            res=max(res,high-low+1)
        return res
                