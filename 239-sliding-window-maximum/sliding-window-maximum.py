from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxq=deque()
        res=float('-inf')
        ans=[]
        for i in range(0,k):
            while maxq and nums[maxq[-1]] <= nums[i]:
                maxq.pop()
            maxq.append(i)
        
        ans.append(nums[maxq[0]])
        low=1

        high=k
        while high <len(nums):
            if maxq and maxq[0] < low:
                maxq.popleft()
            while maxq and nums[maxq[-1]] <= nums[high]:
                maxq.pop()
            maxq.append(high)
            
            ans.append(nums[maxq[0]])
            low+=1
            high+=1

        return ans

