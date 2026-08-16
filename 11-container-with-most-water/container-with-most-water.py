class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        low=0
        high=n-1
        ans=0
        maxarea=0
        while low<high:
            if height[low] < height[high]:
                ans=height[low] * (high-low)
                maxarea= max(ans,maxarea)
                low+=1
            elif height[low] >= height[high]:
                ans=height[high] * (high-low)
                maxarea= max(ans,maxarea)
                high-=1
        return maxarea

