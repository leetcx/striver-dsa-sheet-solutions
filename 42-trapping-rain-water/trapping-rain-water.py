class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0] * len(height)
        leftmax[0]=height[0]
        rightmax=[0] * len(height)
        rightmax[len(height)-1]=height[len(height)-1]
        n=len(height)
        total=0
        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],height[i])
        for i in range(n-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        for i in range(n):
            total+=min(leftmax[i],rightmax[i])-height[i]
        return total
        