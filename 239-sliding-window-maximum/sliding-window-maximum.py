from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        low=0
        high=0
        q=deque()
        ans=[]
        while high<len(nums):
            while q and nums[q[-1]] <= nums[high]:
                q.pop()      
            q.append(high)
            if q[0] < low:
                q.popleft()
            if high-low+1==k:
                ans.append(nums[q[0]])
                low+=1
            high+=1
        return ans