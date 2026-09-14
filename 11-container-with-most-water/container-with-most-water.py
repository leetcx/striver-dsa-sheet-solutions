class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        res=float('-inf')
        while low<high:
            if height[low]<height[high]:
                area=height[low] * (high-low)
                res=max(res,area)
                low+=1
            else:
                area=height[high] * (high-low)
                res=max(res,area)
                high-=1
        return res