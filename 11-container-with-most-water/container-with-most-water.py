class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        res=float('-inf')
        while low<high:
            cal=(high-low) * min(height[low],height[high])
            res=max(res,cal)
            if height[low] < height[high]:
                low+=1
            else:
                high-=1
        return res